from drinks.models.base import BaseModel, BaseManager
from django.db import models


class FactoryManager(BaseManager):
    pass

class Factory(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + " - " + self.address
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }