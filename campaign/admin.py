from django.contrib import admin
from campaign.models import Campaign

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):    
    prepopulated_fields = { 'slug' : ('title',), }
    list_display = ['title', 'goal', 'balance', 'created_on', 'deadline',]
    
admin.site.register(Campaign, CampaignAdmin)