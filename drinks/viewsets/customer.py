from drinks.models import Customers
from django.http import JsonResponse
from drinks.serializers import CustomersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet


class CustomerViewSet(ReadOnlyModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
