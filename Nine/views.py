from django.shortcuts import render
from django.http import HttpResponse
from .models import Category 


def hi_func(request):

    queryset = Category.objects.all()
    
    return render(request, 'front.html', {'name': 'Omer','result' : list(queryset)})
