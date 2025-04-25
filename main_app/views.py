# main_app/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bird

# class Bird:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Bird instances
# birds = [
#     Bird('Amazon Parrot','baby Amazon Parrot' ,'Chatterbox jungle clown .', 12),
#     Bird('Arican Gray', 'baby Arican Gray','Feathery smartmouth diva.', 10),
#     Bird('Bailey', 'baby Bailey', 'Barky cuddle monster.', 2),
#     Bird('Black Falcon','baby Black Falcon' , 'Sneaky screecher.', 6),
# ]

# main-app/views.py

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age']


def home(request):
    return render(request, 'home.html')


def about(request):
          return render(request, 'about.html')

def bird_index(request):
    birds = Bird.objects.all()  # look familiar?
    return render(request, 'birds/index.html', {'birds': birds})


def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})

