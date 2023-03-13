from django.http import HttpResponse
from django.shortcuts import render
from .models import ApiKeys
# Create your views here.


def index(request):
    apiDetails = ApiKeys.objects.all()
    return render(request, 'index.html', {'apiDetails': apiDetails})
