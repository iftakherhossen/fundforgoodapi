from django.db import models

# Create your models here.
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    ratings = models.CharField(max_length=10, choices=STAR_CHOICES)
    
    def __str__(self):
        return f"{self.review} Reviewed by {self.name}"