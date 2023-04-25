from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Password

# dummy password data for prototyping 
# class Password:
#    def __init__(self, services, useranme, password ):
#        self.services = services
#        self.username = useranme
#        self.password = password

# passwords = [
#     Password('Netflix', 'testtingemail@gmail.com', 'Level#leeyah' ),
#     Password('Hulu', 'testingemail@gmail.com', 'Rememberthis#nf'),
#     Password('Disney+', 'testingemail@gmail.com', 'You-bishvl'),
# ]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def passwords_index(request): 
    passwords = Password.objects.all()
    return render(request, 'passwords/index.html', {'passwords':passwords})

def passwords_detail(request, password_id): 
   password =  Password.objects.get(id=password_id) 
   return render(request, 'passwords/detail.html', {'password': password})


class PasswordCreate(CreateView):
    model = Password
    fields = '__all__'
    template_name = 'passwords/password_form.html'

