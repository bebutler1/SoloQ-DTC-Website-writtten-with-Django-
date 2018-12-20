
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.opt1, name='Option1'), #points to the opt1 function for the initial url, which is just the ip address right now
    path('run1/', views.run1, name ='First Tab'), #points to the run1 function when the url has run1/ at the end

    ]
