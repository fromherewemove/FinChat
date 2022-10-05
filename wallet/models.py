import email
from django.db import models
from account.models import Customuser

# Create your models here.



# this wallet model will hold wallet information but is not a direct refrence to the actual virtual wallet
class Wallet(models.Model):
    user = models.ForeignKey(Customuser, on_delete = models.SET_NULL, null=True)
    balance = models.DecimalField(max_digits=100, default=0, decimal_places=2)
    account_name = models.CharField(max_length=250, default="")
    account_number = models.IntegerField(default=0)
    bank = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=200)
    
    
    # additional fields will be added later
    
    







    # "firstName": "King",
    # "lastName": "Pharoah",
    # "email": "Pharoah@egypt.com",
    # "phoneNumber": "2346544446875",
    # "bvn": null,
    # "password": "56fi4stg2p27krcqji02",
    # "dateOfBirth": "1945-01-12",
    # "dateSignedup": "8/30/2021 7:06:51 PM",
    # "accountNumber": null,
    # "bank": null,
    # "accountName": null,
    # "availableBalance": 0