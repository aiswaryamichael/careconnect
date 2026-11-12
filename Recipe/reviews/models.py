from django.contrib.auth.models import User
from django.db import models

from recipes.models import Recipes


class Review(models.Model):

    recipe=models.ForeignKey(Recipes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
