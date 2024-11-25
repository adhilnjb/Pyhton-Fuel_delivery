from django.urls import path,include
from Admin import views
app_name="Webadmin"
urlpatterns = [
    
    path('district/',views.district,name="district"),
    path('deldistrict/<int:did>',views.Deldistrict,name="Deletedistrict"),
    path('updatedistrict/<int:did>',views.updatedistrict,name="updatedistrict"),
    path('fueltype/',views.fueltype,name="fueltype"),
    path('updatefueltype/<int:did>',views.updatefueltype,name="updatefueltype"),
    path('delfueltype/<int:did>',views.Delfueltype,name="Deletefueltype"),
    path('place/',views.place, name="place"),
    path('delplace/<int:did>',views.Delplace,name="Deleteplace"),
    path('updateplace/<int:did>',views.updateplace,name="updateplace"),
    path('fuelrate/',views.fuelrate,name="fuelrate"),
    path('updatefuelrate/<int:did>',views.updatefuelrate,name="updatefuelrate"),
    path('delfuelrate/<int:did>',views.Delfuelrate,name="Deletefuelrate"),
    path('vehicle/',views.Vehicle,name="Vehicle"),
    path('delvehicle/<int:did>',views.DeleteVehicle,name="DeleteVehicle"),
    path('editvehicle/<int:eid>',views.EditVehicle,name="EditVehicle"),
    path('Location/',views.Location,name="Location"),
    path('dellocation/<int:did>',views.DeleteLocation,name="DlteLocation"),
    path('ajaxplace/',views.AjaxPlace,name="Ajaxplace"),
    path('dealerverify/',views.DealerVerify,name="DealerVerify"),
    path('acceptdealer/<int:aid>',views.acceptdealer,name="acceptdealer"),
    path('rejectdealer/<int:rid>',views.rejecteddealer,name="rejectdealer"),
    path('towingagentverify/',views.AgentVerify,name="TowingAgentVerify"),
    path('accepttowingagent/<int:aid>',views.accepttowingagent,name="acceptagent"),
    path('rejectedtowingagent/<int:rid>',views.rejectedtowingagent,name="rejectagent"),
    path('home/',views.Home,name="Home"),
    path('viewcomplaint/',views.ViewComplaint,name="viewcomplaint"),
    path('reply/<int:cid>',views.Reply,name="reply"),
    path('viewfeedback/',views.ViewFeedback,name="viewfeedback"),
    path('logout/',views.logout,name="Logout"),
]

