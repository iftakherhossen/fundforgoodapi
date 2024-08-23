from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from .models import Campaign
from .serializers import CampaignSerializer
from rest_framework.response import Response

# Create your views here.
class CampaignPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = page_size
    max_page_size = 100
    
class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    pagination_class = CampaignPagination
    # filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get('slug', None)

        if slug:
            queryset = queryset.filter(slug=slug)

        return queryset.order_by('isFulfilled')
    
class RandomCampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        campaigns = Campaign.objects.filter(isFulfilled=False)
        campaigns = campaigns.order_by('deadline')
        return campaigns[:10]