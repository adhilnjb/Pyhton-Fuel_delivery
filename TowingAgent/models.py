from django.db import models
from Guest.models import tbl_towingagent
from Admin.models import tbl_towingvehicletype

# Create your models here.
class tbl_vehicledetails(models.Model):
    vehicle_details=models.CharField(max_length=100)
    vehicle_image=models.FileField(upload_to='vehicle/')
    agent=models.ForeignKey(tbl_towingagent,on_delete=models.CASCADE)
    vtype=models.ForeignKey(tbl_towingvehicletype,on_delete=models.CASCADE)