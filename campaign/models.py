from django.db import models
from user.models import UserModel

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    balance = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)    
    created_on = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    isFulfilled = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f"{self.title}"
        
    def update_balance(self, amount):
        self.contributors += 1
        self.balance += amount
        self.isFulfilled = self.balance >= self.goal
        self.save()