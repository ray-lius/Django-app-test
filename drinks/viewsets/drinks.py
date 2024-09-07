
from drinks.models import Drink
from django.http import JsonResponse
from drinks.serializers import DrinkSerializer, SalesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet

# class Sales(BaseModel):
#     drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total = models.DecimalField(max_digits=5, decimal_places=2)
#     sales_date = models.DateTimeField(auto_now_add=True)

class DrinkViewSet(ReadOnlyModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    
    # link to sales model, add sales history to drink when calling the drink endpoint
    # add sales history as a array when call this list function 
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for drink in serializer.data:
            drink_instance = Drink.objects.get(id=drink['id'])
            drink['sales_history'] = SalesSerializer(drink_instance.sales_set.all(), many=True).data
        return Response(serializer.data)