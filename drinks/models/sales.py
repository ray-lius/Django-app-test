from drinks.models.base import BaseModel, BaseManager
from django.db import models

from drinks.models import Drink
from drinks.models import Customers


class SalesManager(BaseManager):
    pass

class Sales(BaseModel):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    sales_date = models.DateTimeField(auto_now_add=True)
    
    
    
    objects = SalesManager()

    def __str__(self):
        return self.drink.name + " - " + self.customer.name + " - " + str(self.quantity) + " - " + str(self.total) + " - " + str(self.sales_date)
    