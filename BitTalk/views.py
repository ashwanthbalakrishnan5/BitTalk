from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'bittalk/index.html')
