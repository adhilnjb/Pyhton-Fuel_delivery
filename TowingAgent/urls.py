
from django.urls import path,include
from TowingAgent import views
app_name="webagent"
urlpatterns = [

path('Changepassword/',views.Changepassword,name="Changepassword"),
path('Editprofile/',views.Editprofile,name="Editprofile"),
path('Myprofile/',views.Myprofile,name="MyProfile"),
path('home/',views.Home,name="Home"),
path('Vehicle/',views.Vehicle,name="Vehicle"),
path('deletevehicle/<int:did>',views.DeleteVehicle,name="deletevehicle"),
path('userbooking/',views.AgentBooking,name="UserBooking"),
path('AcceptBooking/<int:aid>',views.AcceptBooking,name="AcceptBooking"),
path('RejectBooking/<int:rid>',views.RejectBooking,name="RejectBooking"),
path('logout/',views.logout,name="Logout"),

]


