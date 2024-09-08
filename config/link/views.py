from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404

from link.models import Link, NameLink

from sortinghat.models import Name
import sortinghat.views as sortinghat

# Create your views here.

def open_link(request, uuid):
    try:
        uuid = Link.objects.get(uuid=uuid)
    except Link.DoesNotExist:
        raise Http404("Link does not exist")

    return sortinghat.sortinghat(request)

def sh_view_names(request, uuid):
    names = Name.objects.filter(user=request.user)
    print(names)
    return render(request, 'sortinghat/viewnames.html', {'names': names})

def sh_add_names(request, uuid):
    pass 

    # link = get_object_or_404(Link, uuid=uuid, user=request.user)
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     house = request.POST.get('house')
    #     new_name = Name.objects.create(name=name, house=house, user=request.user)
    #     NameLink.objects.create(link=link.id, name=new_name)
    #     return HttpResponseRedirect(reverse('view_names', args=[uuid]))
    # return render(request, 'sortinghat/addname.html', {'link': link})


@login_required(login_url='/login')
def view_links(request, user):
    if request.user.username != user:
        return HttpResponseForbidden()
    
    links = Link.objects.filter(user=request.user)
    links = [link.serialize() for link in links]

    return render(request, 'link/view_links.html', {'links': links})

@login_required(login_url='/login')
def generate_link(request):
    try:
        Link.objects.create(user=request.user)
    except:
        raise Http404("Error creating link")

    return HttpResponseRedirect(reverse('view_links', args=[request.user.username]))