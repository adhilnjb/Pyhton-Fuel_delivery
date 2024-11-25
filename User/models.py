from django.db import models
from Admin.models import *
from Guest.models import *
from TowingAgent.models import tbl_vehicledetails
# Create your models here.
class tbl_fuelbooking(models.Model):
    fbooking_date=models.DateField(auto_now_add=True)
    fbooking_status=models.CharField(default=0,max_length=5)
    fbooking_amount=models.IntegerField(max_length=50,default=0)
    fueltype=models.ForeignKey(tbl_fueltype,on_delete=models.CASCADE)
    location=models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    fbooking_address=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    dealer=models.ForeignKey(tbl_dealer,on_delete=models.CASCADE)
    payment_status=models.CharField(default=0,max_length=10)
    fbooking_qty=models.IntegerField(max_length=50,default=0)

class tbl_agentbooking(models.Model):
    location=models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    abooking_address=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    vdetails=models.ForeignKey(tbl_vehicledetails,on_delete=models.CASCADE)
    abooking_date=models.DateField(auto_now_add=True)
    abooking_status=models.CharField(default=0,max_length=5)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=100)
    complaint_status=models.CharField(default=0,max_length=5)
    complaint_reply=models.CharField(default="Not replied yet",max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)