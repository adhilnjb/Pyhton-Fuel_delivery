from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
       num1=int(request.POST.get("number1"))
       num2=int(request.POST.get("number2"))
       sum=num1+num2
       return render(request,"basic/sum.html",{"Result":sum})
    else:
        return render(request,"basic/sum.html")

def calculator(request): 
    if request.method=="POST":
       num1=float(request.POST.get("num1"))
       num2=float(request.POST.get("num2"))
       operater=request.POST.get("button")
       if operater=="+":
            Result=num1+num2
            return render(request,"basic/calculator.html",{"Result":Result})
       elif operater=="-":
            Result=num1-num2 
            return render(request,"basic/calculator.html",{"Result":Result})
       elif operater=="*":
            Result=num1*num2 
            return render(request,"basic/calculator.html",{"Result":Result})
       elif operater=="/":
            Result=num1/num2  
            return render(request,"basic/calculator.html",{"Result":Result})
       else:
            return render(request,"basic/calculator.html")
    else:
            return render(request,"basic/calculator.html")

def bio(request):
    if request.method=="POST":
      name1=request.POST.get("fname")
      name2=request.POST.get("lname")
      name=name1+" "+name2
      gender=request.POST.get("female")
      Marital=request.POST.get("marital")
      Department=request.POST.get("department")
      Salary=int(request.POST.get("salary")) 
      if 10000<Salary:
         TA=.4*Salary
         DA=.35*Salary
         HRA=.30*Salary
         LIC=.25*Salary
         PF=.20*Salary
      elif 5000< Salary<10000: 
         TA=.35*Salary
         DA=.30*Salary
         HRA=.25*Salary
         LIC=.20*Salary
         PF=.15*Salary
      elif 5000 <Salary:
         TA=.30*Salary
         DA=.25*Salary
         HRA=.20*Salar
         LIC=.20*Salary
         PF=.10*Salary
      else:  
         return render(request,"basic/bio.html")
      deduction=LIC+PF
      Net_amound=Salary+TA+DA+HRA-deduction

      return render(request,"basic/bio.html",{"name":name,"Gender":gender,"Marital":Marital,"Department":Department,"Salary":Salary,"TA":TA,"DA":DA,"HRA":HRA,"LIC":LIC,"PF":PF,"deduction":deduction,"Netamound":Net_amound })
    
    else: 
          return render(request,"basic/bio.html")
