from django.db import models
from content.model_lists import *
from djmoney.models.fields import MoneyField
from djmoney.money import Money
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cell_number = models.CharField(max_length=100,blank=True,null=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    street_number = models.CharField(max_length=6, blank=True,null=True)
    street_name = models.CharField(max_length=100, blank=True,null=True)
    street_type = models.CharField(verbose_name="Street type",choices=street_choices,max_length=4, blank=True,)
    location_city = models.CharField(verbose_name="City",max_length=100, blank=True,)
    location_state = models.CharField(verbose_name="State",choices=state_validation_choices,max_length=2, blank=True,)
    location_zip = models.CharField(max_length=5, blank=True,null=True)
    credit_score = models.CharField(max_length=3, blank=True, null=True)

class BankAccount(models.Model):
    bank_name = models.CharField(max_length=100,blank=True,null=True)
    account_ending = models.CharField(max_length=100,blank=True,null=True)
    account_nickname = models.CharField(max_length=100,blank=True,null=True)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
