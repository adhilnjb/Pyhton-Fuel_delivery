from django.urls import path,include
from basic import views

urlpatterns = [
    path('Addition/',views.Sum),
    path('calculator/',views.calculator),
    path('bio/',views.bio),
]



