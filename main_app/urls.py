from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('passwords/', views.passwords_index, name='passwords_index'),
    path('passwords/<int:password_id>/', views.passwords_detail, name='passwords_detail'),
    path('passwords/create/', views.PasswordCreate.as_view(), name='password_create'),
    path('passwords/<int:pk>/update/', views.PasswordUpdate.as_view(), name='password_update'), 
    path('passwords/<int:pk>/delete/', views.PasswordDelete.as_view(), name='password_delete'), 
]