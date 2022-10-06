from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from wallet.models import Wallet
from .api import WalletClient
from account.models import Customuser
# Create your views here.

# wallet_client is initialized using our secret and public keys

wallet_client = WalletClient("f4hmj9qvpnp6", "2arf5cse254s")


def profile(request):
    details = Customuser.objects.filter(user=request.user)
    args = {'user': details}
    
    return render(request, 'wallet/hello.html', args)

def acc(request):
    detal = Customuser.objects.filter(user=request.user)
    return detal[0]
    
def generate(request):
    new = acc(request)
    new_wallet = wallet_client.generate_wallet(
        first_name=new.first_name, 
        last_name=new.last_name,
        email=new.email,
        bvn=new.bvn,
        date_of_birth=new.date_of_birth.strftime('%Y-%m-%d')
    )


    # code '200' means it has succeded
    # password and phone_number are automatically retrieved on generate
    if new_wallet['response']['responseCode'] == '200':
        new.verified = True
        new.save()
        Wallet.objects.create(
            user = new,
            balance = new_wallet["data"]["availableBalance"],
            account_name = new_wallet["data"]["accountName"],
            account_number = new_wallet["data"]["accountNumber"],
            bank = new_wallet["data"]["bank"],
            phone_number = new_wallet["data"]["phoneNumber"],
            password = new_wallet["data"]["password"]
        )
        messages.success(request, "Account verified, wallet successfully created")
        return redirect("accounts/home.html")
    else:
        messages.error(request, new_wallet["response"]["message"])

        # sets the password in the wallet africa server as our users password
      