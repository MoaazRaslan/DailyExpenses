from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'name')
        app_label = 'customer'

    def __str__(self):
        return f"{self.user.username} : {self.name}"

