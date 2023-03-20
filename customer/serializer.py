from rest_framework import serializers
from .models import Customer, AccountDetails, Arrears



class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id','user_id','account_number', 'date_of_birth', 'title', 'address']


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['customer', 'account_type', 'date_created']




class ArrearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrears
        fields = ['customer', 'balance']

