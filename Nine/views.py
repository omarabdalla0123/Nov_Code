from django.shortcuts import render
from django.http import HttpResponse


def hi_func(request):


    
    return render(request, 'front.html', {'name': 'Omer'})
