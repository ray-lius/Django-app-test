from drinks.models import Sales
from django.http import JsonResponse
from drinks.serializers import SalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet

class SalesViewSet(ReadOnlyModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer