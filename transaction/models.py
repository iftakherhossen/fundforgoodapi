from django.db import models
from user.models import UserModel
from campaign.models import Campaign

# Create your models here.
TRANSACTION_TYPE = [
    ('Deposit', 'Deposit'),
    ('Donation', 'Donation')
]

class Transaction(models.Model):
    account = models.ForeignKey(UserModel, related_name='user_details', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name='campaign_details', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    balance_after_transaction = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']