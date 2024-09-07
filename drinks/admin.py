from django.contrib import admin
from .models import Drink, Customers, Sales, DrinkFactoryAssociation, Factory

admin.site.register(Drink)
admin.site.register(Customers)
admin.site.register(Sales)
admin.site.register(DrinkFactoryAssociation)
admin.site.register(Factory)
