from django.db import models # type: ignore
import uuid
from django.contrib.auth.models import User # type: ignore


# Create your models here.
class Persons(models.Model):
    username = models.CharField(max_length=100,default="None")
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    upi = models.CharField(max_length=100,default="none")
    wallet = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class LatestCamp(models.Model):
    camp_secret = models.CharField(max_length=100,default="none")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    expire = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    terms_cond = models.TextField()
    is_format = models.BooleanField(default=False)
    _time = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.camp_secret

class CampHistory(models.Model):
    _campID = models.CharField(max_length=1000,default="100000")
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    ip_address = models.CharField(max_length=200,default="none")
    email = models.EmailField(max_length=100,default="none")
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)
    is_verified = models.BooleanField(default=False)
    amount = models.IntegerField()
    is_rejected = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    


'''class PaymentDetails(models.Model):
    email = models.CharField(default="none",max_length=1000)
    amount = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)
    '''

class Withdraw_history(models.Model):
    email = models.CharField(max_length=100, default="none")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField(default=0)
    
    date_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_verified = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
