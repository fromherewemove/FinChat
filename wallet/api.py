from email import header
from urllib import response
from wsgiref import headers
import requests
import json


# walletclient will act as a connection between the user and api

class WalletClient:

    def __init__(self, secret_key, public_key):
        self.url = "https://api.wallets.africa"
        self.sandbox = "https://sandbox.wallets.africa"
        self.secret_key = secret_key
        self.public_key = public_key

    def generate_wallet(self, first_name, last_name, email, bvn, date_of_birth):
        url = self.sandbox + "/wallet/generate"
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "Bvn": bvn,
            "email": email,
            "dateOfBirth": date_of_birth,
            "currency": "NGN",
            "secretKey": self.secret_key,
        }

        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=100)
        except Exception as e:
            raise e

    def get_balance(self, phone_number):
        url = self.sandbox + "/wallet/balance"
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        payload = {
            "phoneNumber": phone_number,
            "currency": "NGN",
            "secretKey": self.secret_key
        }

        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=100)
        except Exception as e:
            raise e
        resp = json.loads(r.text, strict=False)
        return resp

    def credit_wallet(self, amount, sender_phone_number, transaction_reference):
        url = self.sandbox + "/wallet/credit"
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        payload = {
            "transactionReference": transaction_reference,
            "amount": amount,
            "phoneNumber": sender_phone_number,
            "secretKey": self.secret_key
        }
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    def debit_wallet(self, amount, reciever_phone_number, transaction_reference):
        url = self.sandbox + "/wallet/debit"
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        payload = {
            "transactionReference": transaction_reference,
            "amount": amount,
            "phoneNumber": reciever_phone_number,
            "secretKey": self.secret_key
        }
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        except Exception as e:
            raise e

        resp = json.loads(r.text, strict=False)
        return resp

    # password should be set as users own account password
    def set_password(self, phone_number, password):
        url = self.sandbox + "/wallet/password"
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        payload = {
            "phoneNumber": phone_number,
            "password": password,
            "secretKey": self.secret_key
        }

        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        except Exception as e:
            raise e


        resp = json.loads(r.text, strict=False)
        return 
        