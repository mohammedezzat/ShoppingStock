from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Stock
from .serializers import StockSerializer

# Create your views here.

def stock_list(request):
    if request.method == "GET":
        item_stock = Stock.objects.all()
        serializer = StockSerializer(item_stock,many=True)
        return JsonResponse(serializer.data,safe=False)
