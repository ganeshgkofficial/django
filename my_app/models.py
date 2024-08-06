from django.db import models

# Create your models here.


class Food(models.Model):
    food_category = (
        ('veg','veg'),
        ('non','non veg')

    )
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    category = models.CharField(max_length=20,choices = food_category)
