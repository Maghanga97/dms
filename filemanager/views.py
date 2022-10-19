import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import *
from . import utils


# Create your views here.
def registration_view(request):
    msg = None
    if request.method == 'POST':
        route_link = request.POST.get('link-tag')
        user_pass = request.POST.get('user-pass')
        user_name = request.POST.get('username')
        department = request.POST.get('department')
        org = request.POST.get('organization')
        user_mail = request.POST.get('email')
        user_phone = request.POST.get('phone_no')
        msg = 'An error occurred during registration of user'
        try:
            if department != "":
                department = Department.objects.get(name=department)
            else:
                department = None 
            employee = Employee.objects.create_user(username=user_name.lower(), email=user_mail, phone_no=user_phone, password=user_pass,department=department)
            msg = f'You have successfully created user {employee.username}'
        except:
            pass
        if route_link is not None:
            messages.success(request, msg)
            return redirect(f'/{route_link}/')
        messages.success(request, msg)
        return redirect('/register/')
    return render(request, 'dms/register.html', {})

def loginPage(request):
    msg = None
    if request.method == 'POST':
        requesting_user = request.POST.get('username').lower()
        requesting_user_password= request.POST.get('user-pass')
        if Employee.objects.filter(username=requesting_user).exists():
            user = Employee.objects.get(username=requesting_user)
            authenticated_user = authenticate(request, username=requesting_user, password=requesting_user_password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                msg = "Successfully logged in"
                try:
                    del request.session[requesting_user]
                except:    
                    active = request.session[requesting_user] = requesting_user
                return redirect('/')
            else:
                pass
        msg = "The password or the username you entered is incorrect"
        messages.success(request, msg)
        return redirect('/login/')

    return render(request, 'dms/login.html', {})

def logoutPage(request):
    try:
        del request.session[request.user]
    except:
        pass
    logout(request)
    return redirect('/login/')


def share_file(request):
    if request.method == 'POST':
        file_slug = request.POST.get('file-slug')
        share_to_this_user = request.POST.get('user')
        sharing_user = Employee.objects.get(username=request.user)
        user = Employee.objects.get(username=share_to_this_user)
        file = File.objects.get(slug=file_slug)
        print(request.user, file.added_by.username)
        if file.added_by.username != sharing_user.username:
            messages.error(request, "You do not have the permission to share this file, request file owner to make the share")
            return redirect('/')

        if FileShare.objects.filter(file=file, user=user).exists():
            messages.error(request, "You have already shared the file")
            return redirect('/')
        fileshare = FileShare.objects.create(file=file, user=user)
        fileshare.save()
        messages.success(request, f"You have successfully shared a file with {user.username}")
    return redirect('/')

@login_required(login_url='/login/')
def load_user_dashboard(request):
    user = Employee.objects.get(username=request.user)
    files = File.objects.filter(added_by=user)
    shared = File.objects.filter(shared_to__username=user.username)
    files = files | shared
    paginator = Paginator(files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    users = Employee.objects.all()

    return render(request, 'dms/admin.html', {'files': page_obj, 'user_files': files, 'logged_user': user, 'users': users})

@login_required(login_url='/login/')
def add_file(request):
    form = AddFile()
    if request.method == 'POST':
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            file_owner = Employee.objects.get(username=request.user)
            new_file = form.save()
            new_file.added_by = file_owner
            new_file.save()
            messages.success(request, 'File was added successfully')
            return redirect('/add-file/')

    return render(request, 'dms/add-file.html', {'form': form})

@login_required(login_url='/login/')
def settings(request):
    return render(request, 'dms/settings.html', {})