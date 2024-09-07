from drinks.models.base import BaseModel, BaseManager
from django.db import models

class CustomersManager(BaseManager):
    pass

class Customers(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = CustomersManager()
    
    def __str__(self):
        return self.name + " - " + self.phone + " - " + str(self.age)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "age": self.age,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }