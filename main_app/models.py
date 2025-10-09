from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    text = models.TextField(max_length=500)
    image_url = models.ImageField(upload_to='uploads/')
    url_project = models.TextField()

class Contacts(models.Model):
    mail = models.CharField(max_length=100)
    tiktok = models.CharField(max_length=100, null=True)
    telegram = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)

class InfoForPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='uploads/')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    type_of_activity = models.TextField(max_length=100)
    about = models.TextField(max_length=500)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=100)


