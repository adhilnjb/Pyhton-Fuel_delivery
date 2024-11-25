
from django.urls import path,include
from User import views
app_name="webuser"
urlpatterns = [

path('Changepassword/',views.Changepassword,name="Changepassword"),
path('Editprofile/',views.Editprofile,name="EditProfile"),
path('Myprofile/',views.Myprofile,name="MyProfile"),
path('home/',views.Home,name="Home"),
path('search/',views.SearchDealer,name="SearchDealer"),
path('ajaxsearch/',views.AjaxSearch,name="Ajaxsearch"),
path('fuelbooking/<int:did>',views.fuelbooking,name="fuelbooking"),
path('Ajaxgetrate/',views.Ajaxgetrate,name="Ajaxgetrate"),
path('Ajaxlocation/',views.Ajaxlocation,name="AjaxLocation"),
path('MyFuelbooking/',views.MyFuelbooking,name="MyFuelbooking"),
path('Fuelpay/<int:bid>',views.fuelpay,name="Fuelpay"),
path('searchagent/',views.SearchAgent,name="SearchAgent"),
path('ajaxsearchagent/',views.AjaxSearchAgent,name="AjaxSearchAgent"),
path('vehicles/<int:aid>',views.ViewVehicle,name="vehicles"),
path('agentbooking/<int:bid>',views.AgentBooking,name="AgentBooking"),
path('AjaxVehicle/',views.AjaxVehicle,name="AjaxVehicle"),
path('MyAgentbooking/',views.MyAgentbooking,name="MyAgentbooking"),
path('complaint/',views.Complaint,name="complaint"),
path('delcomplaint/<int:did>',views.DelComplaint,name="DeleteComplaint"),
path('editcomplaint/<int:eid>',views.EditComplaint,name="EditComplaint"),
path('feedback/',views.Feedback,name="feedback"),
path('delfeedback/<int:did>',views.DelFeedback,name="DeleteFeedback"),
path('editfeedback/<int:eid>',views.EditFeedback,name="EditFeedback"),
path('logout/',views.logout,name="Logout"),
]


