# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


# views.py

class Bird:
    def __init__(self, name,breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Bird instances
birds = [
    Bird('Amazon Parrot','baby Amazon Parrot' ,'Chatterbox jungle clown .', 12),
    Bird('Arican Gray', 'baby Arican Gray','Feathery smartmouth diva.', 10),
    Bird('Bailey', 'baby Bailey', 'Barky cuddle monster.', 2),
    Bird('Black Falcon','baby Black Falcon' , 'Sneaky screecher.', 6)
]



def home(request):
    return render(request, 'home.html')

def about(request):
          return render(request, 'about.html')

def bird_index(request):
 
    return render(request, 'birds/index.html', {'birds': birds})
