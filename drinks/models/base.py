import logging
from django.db import models
from django.db.models import Q, ManyToManyField, ForeignKey, ForeignObject, OneToOneField, ForeignObjectRel, \
    ManyToOneRel, ManyToManyRel, OneToOneRel, QuerySet


logger = logging.getLogger(__name__)

class BaseManager(models.Manager):
    pass

class BaseModel(models.Model):

    class Meta:
        abstract = True
        
    @classmethod
    def get_fields(cls):
        return [field.name for field in cls._meta.get_fields()]
    
    @classmethod
    def get_base_fields(cls):
        base_fields = set()
        for field in cls._meta.get_fields():
            if isinstance(field, (ManyToManyField, ForeignKey, ForeignObject, OneToOneField, ForeignObjectRel, ManyToOneRel, ManyToManyRel, OneToOneRel)):
                continue
            base_fields.add(field.name)
        return list(base_fields)