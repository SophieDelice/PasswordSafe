from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home), 
    path('about/', views.about),
    path('passwords/', views.passwords_index),
    path('passowrds/<int:password_id>/', views.passwords_detail),
]
