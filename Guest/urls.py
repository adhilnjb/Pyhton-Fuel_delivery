
from django.urls import path,include
from Guest import views
app_name="webGuest"
urlpatterns = [


  path('dealer/',views.dealer,name="Dealer"),
  path('TowingAgent/',views.TowingAgent,name="Agent"),
  path('Login/',views.Login,name="Login"),
  path('User/',views.User,name="User"),
  path('',views.index,name="index"),


]