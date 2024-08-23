from rest_framework import serializers
from campaign.models import Campaign
from user.serializers import UserSerializer 

class CampaignSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
     
    class Meta:
        model = Campaign
        fields = '__all__'