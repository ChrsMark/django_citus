from django.db import models

# Create your models here.
class Review(models.Model):
    review_string = models.CharField(max_length=120)

class ReviewSharded(models.Model):
    review_id = models.IntegerField()
    review_string = models.CharField(max_length=120)
