from rest_framework import serializers
from .models import Transaction
from campaign.serializers import CampaignSerializer
from user.serializers import UserSerializer
from django.contrib.auth.models import User

class TransactionSerializer(serializers.ModelSerializer):
    account = UserSerializer(required=False, allow_null=True)
    campaign = CampaignSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'

class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['campaign', 'amount', 'transaction_type', 'account']