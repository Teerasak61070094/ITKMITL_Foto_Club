from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_Account(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    student_id = models.CharField(max_length=8)
    picture_path = models.URLField(max_length = 500,null = True)
    audience = models.BooleanField(default=True)
    member = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

class Equipment(models.Model):
    type_for = (('0', 'camera'),('1', 'lens'),('2', 'light'),('3', 'other'))
    equipment_type = models.CharField(max_length=1, choices=type_for)
    equipment_detail = models.TextField()
    equipment_title = models.CharField(max_length=50)

class Request(models.Model):
    request_title = models.CharField(max_length=50)
    location = models.TextField()
    picture_path = models.URLField(max_length = 500,null = True) 
    detail = models.TextField()
    request_status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Request_contact(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)

class Request_Datetime(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(auto_now=True)

class Audience_suggestion(models.Model):
    detail = models.TextField()

class Member_suggestion(models.Model):
    detail = models.TextField()