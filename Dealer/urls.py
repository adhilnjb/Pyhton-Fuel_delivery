from django.urls import path,include
from Dealer import views
app_name="webdealer"
urlpatterns = [


path('Dealer/',views.Dealer,name="MyProfile"),
path('editProfile/',views.editProfile,name="editProfile"),
path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
path('home/',views.Home,name="Home"),
path('fuelbooking/',views.FuelBooking,name="FuelBooking"),
path('AcceptBooking/<int:aid>',views.AcceptBooking,name="AcceptBooking"),
path('RejectBooking/<int:rid>',views.RejectBooking,name="RejectBooking"),
path('logout/',views.logout,name="Logout"),
]