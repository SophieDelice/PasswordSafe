from django.shortcuts import render

# dummy password data for prototyping 
class Password:
   def __init__(self, services, useranme, password ):
       self.services = services
       self.username = useranme
       self.password = password

passwords = [
    Password('Netflix', 777-999-4560, 'Level#leeyah' ),
    Password('Hulu', 'testingemail@gmail.com', 'Rememberthis#nf'),
    Password('Disney+', 'testingemail@gmail.com', 'You-bishvl'),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def passwords_index(request): 
    return render(request, 'passwords/index.html', {'passwords': passwords})