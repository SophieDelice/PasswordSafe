from django.shortcuts import render,reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Passcard
from django.contrib.auth import login
from django.contrib.auth.forms import UserChangeForm

import random
import string
from django.shortcuts import render

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
    passwords = Passcard.objects.all()
    return render(request, 'passwords/index.html', {'passwords':passwords})

def passwords_detail(request, password_id): 
   password =  Passcard.objects.get(id=password_id) 
   return render(request, 'passwords/detail.html', {'password': password})


def generate_password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 8)) 
    else:
        length = 8
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    password = ''.join(random.choice(all_characters) for i in range(length))

    context = {'password': password}
    return render(request, 'password_generator.html', context)


def signup(request): 
    error_message = ''
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('passwords_index')
        else: 
            error_message = 'Invalid sign up - try again'
        
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form, 
        'error': error_message 
    })
       


class PasscardCreate(CreateView):
    model = Passcard
    fields = ('StreamingService', 'username', 'password')
    template_name = 'passwords/password_form.html'
    success_url= '/passwords/'
    def form_valid(self, form ): 
        form.instance.user = self.request.user
        return super().form_valid(form)

class PasscardUpdate(UpdateView): 
    model = Passcard
    fields = '__all__'
    template_name = 'passwords/password_form.html'

class PasscardDelete(DeleteView): 
    model= Passcard
    success_url= '/passwords/'
    template_name = 'passwords/password_confirm_delete.html'
