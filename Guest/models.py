from django.db import models
from Admin.models import *
# Create your models here.
class tbl_dealer(models.Model):
    dealer_name=models.CharField(max_length=20)
    dealer_email=models.CharField(max_length=30)
    dealer_contact=models.CharField(max_length=15)
    dealer_address=models.CharField(max_length=50)
    dealer_password=models.CharField(max_length=20)
    dealer_photo=models.FileField(upload_to='DealerDoc/')
    dealer_proof=models.FileField(upload_to='DealerDoc/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    dealer_vstatus=models.CharField(max_length=5,default=0)

class tbl_towingagent(models.Model):
    agent_name=models.CharField(max_length=20)
    agent_email=models.CharField(max_length=30)
    agent_contact=models.CharField(max_length=15)
    agent_address=models.CharField(max_length=50)
    agent_password=models.CharField(max_length=20)
    agent_photo=models.FileField(upload_to='AgentDoc/')
    agent_proof=models.FileField(upload_to='AgentDoc/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    agent_vstatus=models.CharField(max_length=5,default=0)

class tbl_user(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=15)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=20)
    user_photo=models.FileField(upload_to='UserDoc/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
