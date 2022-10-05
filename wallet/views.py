from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from wallet.models import Wallet
from .api import WalletClient
# Create your views here.

# wallet_client is initialized using our secret and public keys

wallet_client = WalletClient("f4hmj9qvpnp6", "2arf5cse254s")

def generate(request):
    new_wallet = wallet_client.generate_wallet(
        first_name=request.user.first_name, 
        last_name=request.user.last_name,
        email=request.user.email,
        bvn=request.user.customuser.bvn,
        date_of_birth=request.user.customuser.date_of_birth.strftime('%Y-%m-%d')
    )


    # code '200' means it has succeded
    # password and phone_number are automatically retrieved on generate
    if new_wallet["response"]["responseCode"] == '200':
        messages.success(request, "Account verified, wallet successfully created")
        Wallet.objects.create(
            first_name=request.user.first_name, 
            last_name=request.user.last_name,
            email=request.user.email,
            bvn=request.user.customuser.bvn,
            password=request.user.password, 
            phone_number=new_wallet['data']['phoneNumber']
        )

        # sets the password in the wallet africa server as our users password
        wallet_client.set_password(
            phone_number=new_wallet['data']['phoneNumber'],
            password=request.user.password
        )
    else:
        messages.error(request, new_wallet["response"]["message"])
    return HttpResponse("Wallet Generator")