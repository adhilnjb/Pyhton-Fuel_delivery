from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
# Create your views here.

def dealer(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        selplace=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_dealer.objects.create(dealer_name=request.POST.get("txt_name"),
                                  dealer_email=request.POST.get("txt_email"),
                                  dealer_contact=request.POST.get("txt_contant"),
                                  dealer_address=request.POST.get("address"),
                                  dealer_photo=request.FILES.get("photo"),
                                  dealer_proof=request.FILES.get("proof"),
                                  dealer_password=request.POST.get("txt_password"),
                                  place=selplace)
        return render(request,"Guest/dealer.html",{"district":districtdata})
    else:
        return render(request,"Guest/dealer.html",{"district":districtdata})


def TowingAgent(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        selplace=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_towingagent.objects.create(agent_name=request.POST.get("txt_name"),
                                  agent_email=request.POST.get("txt_email"),
                                  agent_contact=request.POST.get("txt_contant"),
                                  agent_address=request.POST.get("address"),
                                  agent_photo=request.FILES.get("photo"),
                                  agent_proof=request.FILES.get("proof"),
                                  agent_password=request.POST.get("txt_password"),
                                  place=selplace)
        return render(request,"Guest/TowingAgent.html",{"district":districtdata})
    else:
        return render(request,"Guest/TowingAgent.html",{"district":districtdata})


    
def Login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        admincount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        dealercount=tbl_dealer.objects.filter(dealer_email=Email,dealer_password=Password,dealer_vstatus=1).count()
        agentcount=tbl_towingagent.objects.filter(agent_email=Email,agent_password=Password,agent_vstatus=1).count()
        usercount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        if admincount>0:
            admin=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session["adminid"]=admin.id
            request.session["adminname"]=admin.admin_name                       
            return redirect("Webadmin:Home")
        elif dealercount>0:
            dealer=tbl_dealer.objects.get(dealer_email=Email,dealer_password=Password,dealer_vstatus=1)
            request.session["dealerid"]=dealer.id
            request.session["dealername"]=dealer.dealer_name
            return redirect("webdealer:Home")
        elif agentcount>0:
            agent=tbl_towingagent.objects.get(agent_email=Email,agent_password=Password,agent_vstatus=1) 
            request.session["agentid"]=agent.id
            request.session["agentname"]=agent.agent_name
            return redirect("webagent:Home")
        elif usercount>0:
            user=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session["userid"]=user.id
            request.session["username"]=user.user_name                       
            return redirect("webuser:Home")
        else:
             return render(request,"Guest/Login.html")
    else:      
        return render(request,"Guest/Login.html")

def User(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        selplace=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_user.objects.create(user_name=request.POST.get("txt_name"),
                                  user_email=request.POST.get("txt_email"),
                                  user_contact=request.POST.get("txt_contant"),
                                  user_address=request.POST.get("txt_address"),
                                  user_photo=request.FILES.get("photo"),
                                  user_password=request.POST.get("txt_password"),
                                  place=selplace)
        return render(request,"Guest/User.html",{"district":districtdata})
    else:
        return render(request,"Guest/User.html",{"district":districtdata})

def index(request):
    return render(request,"Guest/index.html")



