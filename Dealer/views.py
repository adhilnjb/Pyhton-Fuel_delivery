
from django.shortcuts import render,redirect
from Dealer.models import *
from Guest.models import tbl_dealer
from User.models import tbl_fuelbooking
# Create your views here.

def Dealer(request):
    dealer=tbl_dealer.objects.get(id=request.session["dealerid"])
    return render(request,"Dealer/myprofile.html",{"Dealer":dealer})
def editProfile(request):
    dealer=tbl_dealer.objects.get(id=request.session["dealerid"])
    if request.method=="POST":
        dealer.dealer_name=request.POST.get("name")
        dealer.dealer_email=request.POST.get("email")
        dealer.dealer_contact=request.POST.get("contant")
        dealer.dealer_address=request.POST.get("address")
        dealer.save()
        return redirect("webdealer:MyProfile")
    else:
        return render(request,"Dealer/editProfile.html",{"Dealer":dealer})
def ChangePassword(request):
    current=request.POST.get("Current")
    new=request.POST.get("new")
    confirm=request.POST.get("Confirm")
    dealer=tbl_dealer.objects.get(id=request.session["dealerid"])
    if request.method=="POST":
        if dealer.dealer_password == current:
            if new == confirm:
                dealer.dealer_password=new
                dealer.save()
                return redirect("webdealer:MyProfile")
            else:
                return render(request,"Dealer/ChangePassword.html")
        else:
            return render(request,"Dealer/ChangePassword.html")
    else:
        return render(request,"Dealer/ChangePassword.html")
def Home(request):
    if 'dealerid' in request.session:
        name=request.session["dealername"]
        return render(request,"Dealer/Home.html",{"name":name})
    else:
        return render(request,"Guest/Login.html")
    
def FuelBooking(request):
    Dealer=tbl_dealer.objects.get(id=request.session["dealerid"])
    bookings=tbl_fuelbooking.objects.filter(dealer=Dealer)
    return render(request,"Dealer/ViewFuelBooking.html",{"fuelbookings":bookings})

def AcceptBooking(request,aid):
    bookings=tbl_fuelbooking.objects.get(id=aid)
    bookings.fbooking_status=1
    bookings.save()
    return redirect("webdealer:FuelBooking")

def RejectBooking(request,rid):
    bookings=tbl_fuelbooking.objects.get(id=rid)
    bookings.fbooking_status=2
    bookings.save()
    return redirect("webdealer:FuelBooking")

def logout(request):
    if 'dealerid' in request.session:
        del request.session['dealerid']
        return redirect('webGuest:Login')
    else:
        return redirect('webGuest:Login')