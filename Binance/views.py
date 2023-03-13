from .app.get_balance import Balance
from django.http import HttpResponse
from django.shortcuts import render
from .models import ApiKeys
# Create your views here.


def index(request):
    apiDetails = ApiKeys.objects.get(name="Veda")
    balance = Balance(apiDetails.apiKey, apiDetails.secretKey)
    return render(request, 'index.html', {'balance': balance})
