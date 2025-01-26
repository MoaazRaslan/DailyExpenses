from django.db import models
from customer.models import Customer
import datetime
class Order(models.Model):
    name = models.CharField(max_length=30)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    amount = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    payed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.user} {self.customer.name} {self.name}"
    
