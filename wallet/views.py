from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .api import WalletClient
# Create your views here.
wallet_client = WalletClient("f4hmj9qvpnp6", "2arf5cse254s")

def generate(request):
    return HttpResponse(wallet_client.generate_wallet("King", "Pharoah", "222", "Pharoah@egypt.com", "1945-01-12", "NGN").text)
    