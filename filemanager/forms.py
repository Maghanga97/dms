from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import *


class UserGroupForm(ModelForm):
	class Meta:
		model = Group
		fields = '__all__'

class AddFile(ModelForm):
	class Meta:
		model = File
		fields = ('name', 'description', 'slug','file_location')
		widgets = {
			'name': forms.TextInput(attrs={"class":"form-control mb-3", "placeholder":"Enter your file name here..."}),
			'description': forms.Textarea(attrs={'class':"form-control mb-3", "rows":"5", "placeholder": "Provide a short description of your file"}),
			'slug': forms.TextInput(attrs={'placeholder': 'example, this-is-my-file', "class":"form-control mb-3"}),
			'file_location': forms.FileInput(attrs={'class': 'form-control mb-3'}),
		}
        

# forms