from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError  # Add this import statement

from sortinghat.models import Name, NameForm

def sortinghat(request):
    show_setting = False

    if request.user.is_authenticated:
        show_setting = True

    return render(request, 'sortinghat/sortinghat.html',
        {'show_setting': show_setting})

def utils_get_names():

    names = Name.objects.filter()
    return names

def utils_add_name(name, house):

    name = Name(name=name, house=house)
    name.save()

    return name.id
    
def utils_delete_name(id):

    name = Name.objects.get(id=id)
    name.delete()

    return 

def add_name(request):
    message = ''

    if request.method == 'POST':
        name = request.POST['name'].lower()
        house = request.POST['house']

        name = Name(name=name, house=house)
        name.save()

    return HttpResponseRedirect(reverse('view_names'))

def view_names(request):

    if request.method == 'POST':
        add_name(request)

    names = Name.objects.filter()
    return render(request, 'sortinghat/viewnames.html', {
        'names': names,
        'form': NameForm()
        })

def delete_name(request, id):
    name = Name.objects.get(id=id)
    name.delete()
    return HttpResponseRedirect(reverse('view_names'))

def getHouse(request, name):

    try:
        name = Name.objects.filter(name=name.lower()).last()
        if name is None:
            raise Name.DoesNotExist
        house = name.serialize()["house"]
    except Name.DoesNotExist:
        house = None

    return JsonResponse({'house': house}, safe=False)