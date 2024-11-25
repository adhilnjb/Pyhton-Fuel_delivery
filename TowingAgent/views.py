from django.shortcuts import render,redirect
from TowingAgent.models import *
from Guest.models import tbl_towingagent
from Admin.models import tbl_towingvehicletype
from User.models import tbl_agentbooking

def Myprofile(request):
    TowingAgent=tbl_towingagent.objects.get(id=request.session["agentid"])
    return render(request,"TowingAgent/Myprofile.html",{"agent":TowingAgent})
def Editprofile(request):
    TowingAgent=tbl_towingagent.objects.get(id=request.session["agentid"])
    if request.method=="POST":
        TowingAgent.agent_name=request.POST.get("name")
        TowingAgent.agent_email=request.POST.get("email")
        TowingAgent.agent_contact=request.POST.get("contant")
        TowingAgent.agent_address=request.POST.get("address")
        TowingAgent.save()
        return redirect("webagent:MyProfile")
    else:
        return render(request,"TowingAgent/Editprofile.html",{"agent":TowingAgent})
def Changepassword(request):
    current=request.POST.get("Current")
    new=request.POST.get("new")
    confirm=request.POST.get("Confirm")
    TowingAgent=tbl_towingagent.objects.get(id=request.session["agentid"])
    if request.method=="POST":
        if TowingAgent.agent_password == current:
            if new == confirm:
                TowingAgent.agent_password=new
                TowingAgent.save()
                return redirect("webagent:MyProfile")
            else:
                return render(request,"TowingAgent/ChangePassword.html")
        else:
            return render(request,"TowingAgent/ChangePassword.html")
    else:
        return render(request,"TowingAgent/ChangePassword.html")
def Home(request):
    if 'agentid' in request.session:
        name=request.session["agentname"]
        return render(request,"TowingAgent/Home.html",{"name":name})
    else:
        return render(request,"Guest/Login.html")


def Vehicle(request):
    agent=tbl_towingagent.objects.get(id=request.session["agentid"])
    vdetails=tbl_vehicledetails.objects.filter(agent=agent)
    type=tbl_towingvehicletype.objects.all()
    if request.method=="POST":
        agent=tbl_towingagent.objects.get(id=request.session["agentid"])
        seltype=tbl_towingvehicletype.objects.get(id=request.POST.get("sel_type"))
        tbl_vehicledetails.objects.create(vehicle_details=request.POST.get("details"),
                                          vehicle_image=request.FILES.get("photo"),
                                          agent=agent,
                                          vtype=seltype)
        return render(request,"TowingAgent/VehicleDetails.html",{"type":type,"vdetails":vdetails})
    else:
        return render(request,"TowingAgent/VehicleDetails.html",{"type":type,"vdetails":vdetails})
    
def DeleteVehicle(request,did):
    tbl_vehicledetails.objects.get(id=did).delete()
    return redirect("webagent:Vehicle")

def AgentBooking(request):
    Agent=tbl_towingagent.objects.get(id=request.session["agentid"])
    bookings=tbl_agentbooking.objects.filter(vdetails__agent=Agent)
    return render(request,"TowingAgent/ViewUserBooking.html",{"agentbookings":bookings})

def AcceptBooking(request,aid):
    bookings=tbl_agentbooking.objects.get(id=aid)
    bookings.abooking_status=1
    bookings.save()
    return redirect("webagent:UserBooking")

def RejectBooking(request,rid):
    bookings=tbl_agentbooking.objects.get(id=rid)
    bookings.abooking_status=2
    bookings.save()
    return redirect("webagent:UserBooking")

def logout(request):
    if 'agentid' in request.session:
        del request.session['agentid']
        return redirect('webGuest:Login')
    else:
        return redirect('webGuest:Login')