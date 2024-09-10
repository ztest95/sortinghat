from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.db import IntegrityError

from link.models import Link, NameLink

from sortinghat.models import Name, NameForm
import sortinghat.views as sortinghat
import sortinghat.templates as templates
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('view_links', args=[request.user.username]))
    
    return render(request, 'link/home.html')


def open_link(request, uuid):
    try:
        uuid = Link.objects.get(uuid=uuid)
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    
    show_setting = False
    if request.user == uuid.user:
        show_setting = True

    return render(request, 'sortinghat/sortinghat.html',
        {'show_setting': show_setting})


@login_required(login_url='/login')
def sh_view_names(request, uuid):

    if request.user != Link.objects.get(uuid=uuid).user:
        return HttpResponseForbidden

    if request.method == 'POST':
        sh_add_names(request, uuid)

    link = get_object_or_404(Link, uuid=uuid)
    names = NameLink.objects.filter(link=link)
    
    names = [name.serialize() for name in names]

    return render(request, 'link/viewnames.html', {
        'names': names,
        'form': NameForm(),
        'link': link
        })

@login_required(login_url='/login')
def sh_add_names(request, uuid):
    # get form response
    # save name to Name model
    # create namelink with link.id and name.id
    # save namelink

    if request.method == 'POST':
        name = request.POST['name'].lower()
        house = request.POST['house']

        name_id = sortinghat.utils_add_name(name, house)
        name_link = NameLink(link=Link.objects.get(uuid=uuid), name=Name.objects.get(id=name_id))
        
        try:
            name_link.save()
        except:
            raise Http404("Error adding name")

    return HttpResponseRedirect(reverse('view_names', args=[uuid]))

@login_required(login_url='/login') 
def sh_delete_name(request, uuid, id):

    if request.user != Link.objects.get(uuid=uuid).user:
        return HttpResponseForbidden
    
    NameLink.objects.get(link=Link.objects.get(uuid=uuid), name=Name.objects.get(id=id)).delete()
    sortinghat.utils_delete_name(id)

    return HttpResponseRedirect(reverse('view_names', args=[uuid]))

 
@login_required(login_url='/login')
def view_links(request, user):
    if request.user.username != user:
        return HttpResponseForbidden()
    
    links = Link.objects.filter(user=request.user)
    links = [link.serialize() for link in links]

    return render(request, 'link/viewlinks.html', {'links': links})


@login_required(login_url='/login')
def generate_link(request):
    try:
        Link.objects.create(user=request.user)
    except:
        raise Http404("Error creating link")

    return HttpResponseRedirect(reverse('view_links', args=[request.user.username]))