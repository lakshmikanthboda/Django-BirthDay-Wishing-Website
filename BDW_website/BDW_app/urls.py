
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('wish', views.BDWfun),
    #path('/?n=',views.BDWfun)
]