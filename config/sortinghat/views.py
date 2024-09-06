from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from sortinghat.models import Name

@login_required(login_url='/login')
def sortinghat(request):
    return render(request, 'sortinghat/sortinghat.html')

@login_required
def getHouse(request, name):

    if request.method == 'POST':
        pass

    else:

        try:
            name = Name.objects.get(user=request.user, name=name.lower())
            house = name.serialize()["house"]
        except Name.DoesNotExist:
            house = None

        return JsonResponse({'house': house}, safe=False)