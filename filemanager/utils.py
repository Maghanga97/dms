from .models import *


def revoke_file_share(file_id=None, file_slug=None, user=None):
    file = File.objects.get(id=file_id)
    user = Employee.objects.get(username=user)
    fileshare = FileShare.objects.filter(file=file, user=user)
    fileshare.delete()