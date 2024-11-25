from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import tbl_complaint,tbl_feedback,tbl_fuelbooking,tbl_agentbooking
# Create your views here.
def district(request):
    district=tbl_district.objects.all()    
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("district"))
        return render(request,"Admin/district.html",{"Type":district})
    else:
        return render(request,"Admin/district.html",{"Type":district})

def Deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Webadmin:district")

def updatedistrict(request,did):
    district=tbl_district.objects.get(id=did)
    if request.method=="POST":
        district.district_name=request.POST.get("district")
        district.save()
        return redirect("Webadmin:district")
    else:
        return render(request,"Admin/district.html",{"district":district})

def fueltype(request):
    fueltype=tbl_fueltype.objects.all()    
    if request.method=="POST":
        tbl_fueltype.objects.create(fueltype_name=request.POST.get("txtfueltype"))
        return render(request,"Admin/fueltype.html",{"Type":fueltype})
    else:
        return render(request,"Admin/fueltype.html",{"Type":fueltype})

def updatefueltype(request,did):
    fueltype=tbl_fueltype.objects.get(id=did)
    if request.method=="POST":
        fueltype.fueltype_name=request.POST.get("txtfueltype")
        fueltype.save()
        return redirect("Webadmin:fueltype")
    else:
        return render(request,"Admin/fueltype.html",{"fueltype":fueltype})


def Delfueltype(request,did):
    tbl_fueltype.objects.get(id=did).delete()
    return redirect("Webadmin:fueltype") 

def place(request):
   place=tbl_place.objects.all()
   district=tbl_district.objects.all()
   if request.method=="POST":
        selecteddistrict=tbl_district.objects.get(id=request.POST.get("district"))
        tbl_place.objects.create(place_name=request.POST.get("place"),district=selecteddistrict)
        return render(request,"Admin/place.html",{"Type":place,"District":district})
   else:
        return render(request,"Admin/place.html",{"Type":place,"District":district}) 
        
def Delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Webadmin:place")

def updateplace(request,did):
    district=tbl_district.objects.all()
    place=tbl_place.objects.get(id=did)
    if request.method=="POST":
        place.place_name_=request.POST.get("place")
        place.save()
        return redirect("Webadmin:place")
    else:
        return render(request,"Admin/place.html",{"place":place,"District":district})

def fuelrate(request):
   fuelrate=tbl_fuelrate.objects.all()
   fueltype=tbl_fueltype.objects.all()
   if request.method=="POST":
        selectefueltype=tbl_fueltype.objects.get(id=request.POST.get("fueltype"))
        tbl_fuelrate.objects.create(fuelrate_name=request.POST.get("rate"),fueltype=selectefueltype)
        return render(request,"Admin/fuelrate.html",{"Type":fuelrate,"fueltype":fueltype})
   else:
           return render(request,"Admin/fuelrate.html",{"Type":fuelrate,"fueltype":fueltype})

def Delfuelrate(request,did):
    tbl_fuelrate.objects.get(id=did).delete()
    return redirect("Webadmin:fuelrate")

def updatefuelrate(request,did):
    fueltype=tbl_fueltype.objects.all()
    fuelrate=tbl_fuelrate.objects.get(id=did)
    if request.method=="POST":
        fuelrate.fuelrate_name_=request.POST.get("rate")
        fuelrate.save()
        return redirect("Webadmin:fuelrate")
    else:
        return render(request,"Adminfuelrate.html",{"fuelrate":fuelrate,"fueltype":fueltype})


def Vehicle(request):
    vtype=tbl_towingvehicletype.objects.all()
    if request.method=="POST":
        tbl_towingvehicletype.objects.create(vehicle_type=request.POST.get("Vehicle"))
        return render(request,"Admin/TowingVehicleType.html",{"type":vtype})
    else:
        return render(request,"Admin/TowingVehicleType.html",{"type":vtype})
def DeleteVehicle(request,did):
    tbl_towingvehicletype.objects.get(id=did).delete() 
    return redirect("Webadmin:Vehicle")

def EditVehicle(request,eid):
    vtype=tbl_towingvehicletype.objects.get(id=eid)
    if request.method=="POST":
        vtype.vehicle_type=request.POST.get("Vehicle")
        vtype.save()
        return redirect("Webadmin:Vehicle")
    else:
         return render(request,"Admin/TowingVehicleType.html",{"seltype":vtype})

def Location(request):
    district=tbl_district.objects.all()
    location=tbl_location.objects.all()
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_location.objects.create(location_name=request.POST.get("location"),place=placedata)
    return render(request,"Admin/Location.html",{"dis":district,"loc":location})

def DeleteLocation(request,did):
    tbl_location.objects.get(id=did).delete()
    return redirect("Webadmin:Location")

def AjaxPlace(request):
    dist=tbl_district.objects.get(id=request.GET.get("disd"))
    placedata=tbl_place.objects.filter(district=dist)
    return render(request,"Admin/Ajaxplace.html",{"place":placedata})


def DealerVerify(request):
    newdealer=tbl_dealer.objects.filter(dealer_vstatus=0)
    accepted=tbl_dealer.objects.filter(dealer_vstatus=1)
    rejected=tbl_dealer.objects.filter(dealer_vstatus=2)
    return render(request,"Admin/DealerVerification.html",{"New":newdealer,"accepted":accepted,"rejected":rejected})

def acceptdealer(request,aid):
    dealer=tbl_dealer.objects.get(id=aid)
    dealer.dealer_vstatus=1
    dealer.save()
    return redirect("Webadmin:DealerVerify")

def rejecteddealer(request,rid):
    dealer=tbl_dealer.objects.get(id=rid)
    dealer.dealer_vstatus=2
    dealer.save()
    return redirect("Webadmin:DealerVerify")

def AgentVerify(request):
    newdealer=tbl_towingagent.objects.filter(agent_vstatus=0)
    accepted=tbl_towingagent.objects.filter(agent_vstatus=1)
    rejected=tbl_towingagent.objects.filter(agent_vstatus=2)
    return render(request,"Admin/TowingAgentVerification.html",{"New":newdealer,"accepted":accepted,"rejected":rejected})

def accepttowingagent(request,aid):
    dealer=tbl_towingagent.objects.get(id=aid)
    dealer.agent_vstatus=1
    dealer.save()
    return redirect("Webadmin:TowingAgentVerify")

def rejectedtowingagent(request,rid):
    dealer=tbl_towingagent.objects.get(id=rid)
    dealer.agent_vstatus=2
    dealer.save()
    return redirect("Webadmin:TowingAgentVerify")

def Home(request):
    if 'adminid' in request.session:
        aname=request.session["adminname"]
        fuelcount=tbl_fuelbooking.objects.all().count()
        towcount=tbl_agentbooking.objects.all().count()
        usercount=tbl_user.objects.all().count()
        user=tbl_user.objects.all()
        return render(request,"Admin/Home.html",{"name":aname,"count1":fuelcount,"count2":towcount,"count3":usercount,"user":user})
    else:
        return render(request,"Guest/Login.html")
    
def ViewComplaint(request):
    com=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{"new":com,"replied":replied})

def Reply(request,cid):
    com=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("Reply")
        com.complaint_status=1
        com.save()
        return redirect("Webadmin:viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")    
    
def ViewFeedback(request):
    com=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{"new":com})

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        return redirect('webGuest:Login')
    else:
        return redirect('webGuest:Login')