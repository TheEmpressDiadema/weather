from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longtitude = models.DecimalField(max_digits=7, decimal_places=4)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'name', 'latitude', 'longtitude'],
                name='unique_record'
            )
        ]