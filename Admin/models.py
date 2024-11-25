from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)

class tbl_fueltype(models.Model):
    fueltype_name=models.CharField(max_length=20)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_fuelrate(models.Model):
    fuelrate_name=models.CharField(max_length=20)
    fueltype=models.ForeignKey(tbl_fueltype,on_delete=models.CASCADE)

class tbl_towingvehicletype(models.Model):
    vehicle_type=models.CharField(max_length=20)

class tbl_location(models.Model):
    location_name=models.CharField(max_length=20)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_email=models.CharField(max_length=20)
    admin_password=models.CharField(max_length=20)
    