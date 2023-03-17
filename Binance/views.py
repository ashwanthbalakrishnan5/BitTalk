from .app.get_balance import Balance
from .app.get_position_risk import Positions
from django.http import HttpResponse
from django.shortcuts import render
from .models import ApiKeys
# Create your views here.


def index(request):
    return render(request, 'Binance/index.html', {})


def balance(request):
    apiDetails = ApiKeys.objects.get(name="Veda")
    balance = Balance(apiDetails.apiKey, apiDetails.secretKey)
    return render(request, 'Binance/balance.html', {'balance': balance})


def positions(request):
    apiDetails = ApiKeys.objects.get(name="Veda")
    positions = Positions(apiDetails.apiKey, apiDetails.secretKey)
    return render(request, 'Binance/positions.html', {'positions': positions})
