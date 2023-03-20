from django.contrib import admin
from django.conf import settings
from django.db import models



class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.PROTECT)
    account_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField(null=True)
    title = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=2500)

    def __str__(self) -> str:
        return  f'{self.user.first_name} {self.user.last_name }'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name



class AccountDetails(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('GOLD', 'GOLD'),
        ('SILVER', 'SILVER'),
        ('BRONZE', 'BRONZE'),
    ]
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    account_type = models.CharField(max_length=60,choices=ACCOUNT_TYPE_CHOICES, default='BRONZE')
    date_created = models.DateTimeField(auto_now_add=True)



class Arrears(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)
    balance = models.DecimalField(max_digits=9, decimal_places=2)

