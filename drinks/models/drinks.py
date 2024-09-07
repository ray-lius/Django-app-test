from drinks.models.base import BaseModel, BaseManager
from django.db import models
from .factories import Factory

class DrinksManager(BaseManager):
    pass
    
class Drink(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_alcoholic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    factories = models.ManyToManyField(Factory, through='DrinkFactoryAssociation')
    
    objects = DrinksManager()

    def __str__(self):
        return self.name + " - " + self.description
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "is_alcoholic": self.is_alcoholic,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }   
    

class DrinkFactoryAssociationManager(BaseManager):
    pass

class DrinkFactoryAssociation(BaseModel):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = DrinkFactoryAssociationManager()