from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Admin.models import * 
from TowingAgent.models import tbl_vehicledetails
# Create your views here.

def Myprofile(request):
    if 'userid' in request.session:
        user=tbl_user.objects.get(id=request.session["userid"])
        return render(request,"User/Myprofile.html",{"User":user})
    else:
        return render(request,"Guest/Login.html")
def Editprofile(request):
    if 'userid' in request.session:
        user=tbl_user.objects.get(id=request.session["userid"])
        if request.method=="POST":
            user.user_name=request.POST.get("name")
            user.user_email=request.POST.get("email")
            user.user_contact=request.POST.get("contant")
            user.user_address=request.POST.get("address")
            user.save()
            return redirect("webuser:MyProfile")
        else:
            return render(request,"User/Editprofile.html",{"User":user})
    else:
        return render(request,"Guest/Login.html")
def Changepassword(request):
    current=request.POST.get("Current")
    new=request.POST.get("new")
    confirm=request.POST.get("Confirm")
    user=tbl_user.objects.get(id=request.session["userid"])
    if request.method=="POST":
        if user.user_password == current:
            if new == confirm:
                user.user_password=new
                user.save()
                return redirect("webuser:MyProfile")
            else:
                return render(request,"User/Changepassword.html")
        else:
            return render(request,"User/Changepassword.html")
    else:
        return render(request,"User/Changepassword.html")
def Home(request):
    if 'userid' in request.session:
        name=request.session["username"]
        return render(request,"User/Home.html",{"name":name})
    else:
        return render(request,"Guest/Login.html")
    
def SearchDealer(request):
    Dealer=tbl_dealer.objects.filter(dealer_vstatus=1)
    District=tbl_district.objects.all()
    return render(request,"User/SearchDealer.html",{"dealers":Dealer,"district":District})

def AjaxSearch(request):
    if (request.GET.get("dis") != "") and (request.GET.get("plc") != "") :
        district=tbl_district.objects.get(id=request.GET.get("dis"))
        place = tbl_place.objects.get(id=request.GET.get("plc"))
        Dealer=tbl_dealer.objects.filter(place=place,place__district=district,dealer_vstatus=1)
        return render(request,"User/AjaxSearch.html",{'dealers':Dealer})
    elif request.GET.get("dis") != "" :
        district=tbl_district.objects.get(id=request.GET.get("dis"))
        Dealer=tbl_dealer.objects.filter(place__district=district,dealer_vstatus=1)
        return render(request,"User/AjaxSearch.html",{'dealers':Dealer})
    else:
        place = tbl_place.objects.get(id=request.GET.get("plc"))
        Dealer=tbl_dealer.objects.filter(place=place,dealer_vstatus=1)
        return render(request,"User/AjaxSearch.html",{'dealers':Dealer})
    
def fuelbooking(request,did):
    fuel=tbl_fueltype.objects.all()
    district=tbl_district.objects.all()
    if request.method=="POST":
        selfuel=tbl_fueltype.objects.get(id=request.POST.get("sel_fueltype"))
        loc=tbl_location.objects.get(id=request.POST.get("sel_location"))
        user=tbl_user.objects.get(id=request.session["userid"])
        Dealer=tbl_dealer.objects.get(id=did)
        tbl_fuelbooking.objects.create(fbooking_amount=request.POST.get("amnt"),
                                       fueltype=selfuel,
                                       location=loc,
                                       fbooking_address=request.POST.get("txt_address"),
                                       fbooking_qty=request.POST.get("qty"),
                                       user=user,
                                       dealer=Dealer)
        return render(request,"User/Fuelbooking.html",{"Fuel":fuel,"dis":district})
    else:
        return render(request,"User/Fuelbooking.html",{"Fuel":fuel,"dis":district})

def Ajaxgetrate(request):
    fuel=tbl_fueltype.objects.get(id=request.GET.get("fid"))
    rate=tbl_fuelrate.objects.get(fueltype=fuel)
    return render(request,"User/Ajaxgetrate.html",{"rate":rate})

def Ajaxlocation(request):
    place=tbl_place.objects.get(id=request.GET.get("pid"))
    location=tbl_location.objects.filter(place=place)
    return render(request,"User/AjaxLocation.html",{"loc":location})

def MyFuelbooking(request):
    user=tbl_user.objects.get(id=request.session["userid"])
    bookings=tbl_fuelbooking.objects.filter(user=user)
    return render(request,"User/ViewMyFuelBooking.html",{"fuelbookings":bookings})

def fuelpay(request,bid):
    booking=tbl_fuelbooking.objects.get(id=bid)
    amount=booking.fbooking_amount
    if request.method=="POST":
        booking.payment_status=1
        booking.save()
        return redirect("webuser:MyFuelbooking")
    else:
        return render(request,"User/FuelPayment.html",{"total":amount})

def SearchAgent(request):
    Agent=tbl_towingagent.objects.filter(agent_vstatus=1)
    District=tbl_district.objects.all()
    return render(request,"User/SearchTowingAgent.html",{"agents":Agent,"district":District})

def AjaxSearchAgent(request):
    if (request.GET.get("dis") != "") and (request.GET.get("plc") != "") :
        district=tbl_district.objects.get(id=request.GET.get("dis"))
        place = tbl_place.objects.get(id=request.GET.get("plc"))
        Agent=tbl_towingagent.objects.filter(place=place,place__district=district,agent_vstatus=1)
        return render(request,"User/AjaxSearchAgent.html",{'agents':Agent})
    elif request.GET.get("dis") != "" :
        district=tbl_district.objects.get(id=request.GET.get("dis"))
        Agent=tbl_towingagent.objects.filter(place__district=district,agent_vstatus=1)
        return render(request,"User/AjaxSearchAgent.html",{'agents':Agent})
    else:
        place = tbl_place.objects.get(id=request.GET.get("plc"))
        Agent=tbl_towingagent.objects.filter(place=place,agent_vstatus=1)
        return render(request,"User/AjaxSearchAgent.html",{'agents':Agent})

def ViewVehicle(request,aid):
    vtype=tbl_towingvehicletype.objects.all()
    agent=tbl_towingagent.objects.get(id=aid)
    request.session["agid"]=agent.id
    vehicle=tbl_vehicledetails.objects.filter(agent=agent)
    return render(request,"User/ViewVehicles.html",{"data":vehicle,"vtype":vtype})

def AjaxVehicle(request):
    vtype=tbl_towingvehicletype.objects.get(id=request.POST.get("disd"))
    vehicle=tbl_vehicledetails.objects.filter(vtype=vtype)
    return render(request,"User/AjaxSearchVehicle.html",{"data":vehicle})

def AgentBooking(request,bid):
    district=tbl_district.objects.all()
    if request.method=="POST":
        user=tbl_user.objects.get(id=request.session["userid"])
        vdetails=tbl_vehicledetails.objects.get(id=bid)
        sellocation=tbl_location.objects.get(id=request.POST.get("sel_location"))
        tbl_agentbooking.objects.create(abooking_address=request.POST.get("txt_address"),
                                        location=sellocation,
                                        user=user,
                                        vdetails=vdetails)
        return render(request,"User/AgentBooking.html",{"dis":district})
    else:
        return render(request,"User/AgentBooking.html",{"dis":district})
    
def MyAgentbooking(request):
    user=tbl_user.objects.get(id=request.session["userid"])
    bookings=tbl_agentbooking.objects.filter(user=user)
    return render(request,"User/ViewMyAgentBooking.html",{"agentbookings":bookings})

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session["userid"])
    data=tbl_complaint.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["userid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("title"),
                                     complaint_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"User/Complaint.html",{"Data":data})

def DelComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("webuser:complaint")

def EditComplaint(request,eid):
    com=tbl_complaint.objects.get(id=eid)
    if request.method=="POST":
        com.complaint_title=request.POST.get("title")
        com.complaint_content=request.POST.get("complaint")
        com.save()
        return redirect("webuser:complaint")
    else:
        return render(request,"User/Complaint.html",{"com":com})

def Feedback(request):
    userdata=tbl_user.objects.get(id=request.session["userid"])
    data=tbl_feedback.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["userid"])
        tbl_feedback.objects.create(feedback_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"User/Feedback.html",{"Data":data})

def DelFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webuser:feedback")

def EditFeedback(request,eid):
    com=tbl_feedback.objects.get(id=eid)
    if request.method=="POST":
        com.feedback_content_content=request.POST.get("complaint")
        com.save()
        return redirect("webuser:feedback")
    else:
        return render(request,"User/Feedback.html",{"com":com})
    
def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
        return redirect('webGuest:Login')
    else:
        return redirect('webGuest:Login')
