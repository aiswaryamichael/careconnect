from django.db import models

# Create your models here.

class Recipes(models.Model):

    recipe_name=models.CharField(max_length=40)
    ingredients=models.CharField(max_length=100)
    instructions=models.CharField(max_length=100)

    mealtype_choice=(('breakfast','Breakfast'),
                     ('lunch','Lunch'),
                     ('dinner','Dinner'))
    mealtype=models.CharField(max_length=20,choices=mealtype_choice)

    cuisine_choice=(('indian','Indian'),
                   ('italian','Italian'),
                   ('chinese','Chinese'))
    cuisine=models.CharField(max_length=20,choices=cuisine_choice)


