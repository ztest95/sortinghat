from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError  # Add this import statement

from sortinghat.models import Name, NameForm

def sortinghat(request):
    return render(request, 'sortinghat/sortinghat.html')

def add_name(request):
    message = ''

    if request.method == 'POST':
        name = request.POST['name'].lower()
        house = request.POST['house']

        name = Name(name=name, house=house)
        try:
            name.save()
            message = 'Name added successfully'
        except IntegrityError:
            message = 'Error adding name'

    return render(request, 'sortinghat/addname.html', {
        'form': NameForm(),
        'message': message
    })

def view_names(request):
    names = Name.objects.filter()
    return render(request, 'sortinghat/viewnames.html', {'names': names})

def delete_name(request, id):
    name = Name.objects.get(id=id)
    name.delete()
    return HttpResponseRedirect(reverse('view_names'))

def getHouse(request, name):

    if request.method == 'POST':
        pass

    else:

        try:
            name = Name.objects.filter(name=name.lower()).first()
            if name is None:
                raise Name.DoesNotExist
            house = name.serialize()["house"]
        except Name.DoesNotExist:
            house = None

        return JsonResponse({'house': house}, safe=False)