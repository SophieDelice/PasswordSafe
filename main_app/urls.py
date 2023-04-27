from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('passwords/', views.passwords_index, name='passwords_index'),
    path('passwords/<int:password_id>/', views.passwords_detail, name='passwords_detail'),
    path('passwords/create/', views.PasscardCreate.as_view(), name='password_create'),
    path('passwords/<int:pk>/update/', views.PasscardUpdate.as_view(), name='password_update'), 
    path('passwords/<int:pk>/delete/', views.PasscardDelete.as_view(), name='password_delete'), 
    path('accounts/signup/', views.signup, name='signup'), 
    path('generate-password/', views.generate_password, name='generate_password'),
]

  

