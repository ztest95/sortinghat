from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden

from link.models import Link

from sortinghat.views import sortinghat

# Create your views here.

def open_link(request, uuid):
    try:
        uuid = Link.objects.get(uuid=uuid)
    except Link.DoesNotExist:
        return render(request, '404.html')

    return sortinghat(request)

@login_required(login_url='/login')
def view_links(request, user):
    if request.user.username != user:
        return HttpResponseForbidden()
    
    links = Link.objects.filter(user=request.user)

    return render(request, 'link/view_links.html', {'links': links})

@login_required(login_url='/login')
def generate_link(request):
    Link.objects.create(user=request.user)
    return render(reverse('view_links', kwargs={'user': request.user.username}))
