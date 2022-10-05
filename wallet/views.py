from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from wallet.models import Wallet
from .api import WalletClient
# Create your views here.

# wallet_client is initialized using our secret and public keys

wallet_client = WalletClient("f4hmj9qvpnp6", "2arf5cse254s")


def create_wallet(request):
    user = request.user
    new_wallet = wallet_client.generate_wallet(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        date_of_birth = user.date_of_birth.strftime('%Y-%m-%d'),
        bvn = user.bvn

    )
    if new_wallet['reponse']['responseCode'] == '200':
        user.verified = True
        user.save()
        Wallet.objects.create(
            user = user,
                    balance = new_wallet["data"]["availableBalance"],
                    account_name = new_wallet["data"]["accountName"],
                    account_number = new_wallet["data"]["accountNumber"],
                    bank = new_wallet["data"]["bank"],
                    phone_number = new_wallet["data"]["phoneNumber"],
                    password = new_wallet["data"]["password"]

        )
        messages.success(request, "Account Verified, success")
        return redirect('account:home')
    else:
        messages.error(request, new_wallet["response"]["message"])

    return render(request, "wallet/hello.html")