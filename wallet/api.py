from email import header
from urllib import response
from wsgiref import headers
import requests
import json

class WalletClient:

    def __init__(self, secret_key, public_key):
        self.url = "https://api.wallets.africa"
        self.sandbox = "https://sandbox.wallets.africa"
        self.secret_key = secret_key
        self.public_key = public_key

    def generate_wallet(self, firstName, lastName, bvn, email, dob, currency):
        url = self.sandbox + '/wallet/generate'
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "Bvn": bvn,
            "email": email,
            "secretKey": self.secret_key,
            "dateOfBirth": dob,
            "currency": currency
        }
        headers = {'Authorization': "Bearer " + self.public_key, "Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response