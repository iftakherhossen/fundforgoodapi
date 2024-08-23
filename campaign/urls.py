from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CampaignViewSet, RandomCampaignViewSet

router = DefaultRouter()

router.register('list', CampaignViewSet)
router.register('random-campaigns', RandomCampaignViewSet, basename="random_campaigns")

urlpatterns = [
    path('', include(router.urls)),
]