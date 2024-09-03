from django.shortcuts import render

def home(request):
    return render(request, 'sortinghat/home.html')
