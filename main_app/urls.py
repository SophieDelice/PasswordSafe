from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('passwords/', views.passwords_index, name='passwords_index'),
    path('passwords/<int:password_id>/', views.passwords_detail, name='passwords_detail'),
]