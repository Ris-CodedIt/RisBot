from django.contrib import admin
from .models import Customer, AccountDetails, Arrears



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'first_name', 'last_name', 'date_of_birth', 'address', 'title']
    search_fields = ['account_number', 'first_name', 'last_name']
    list_select_related =['user']
    ordering = ['user__first_name']


@admin.register(AccountDetails)
class AccountDetailsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'account_type', 'date_created']
    search_fields = ['customer']
    autocomplete_fields = ['customer']