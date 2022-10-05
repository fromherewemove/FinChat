import email
from django.db import models

# Create your models here.



# this wallet model will hold wallet information but is not a direct refrence to the actual virtual wallet
class Wallet(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length = 12)
    bvn = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    
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