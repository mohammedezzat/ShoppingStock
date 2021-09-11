
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Stock
from .serializers import StockSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def stock_list(request):
    if request.method == "GET":
        gtin = request.GET['gtin']
        shop = request.GET['shop']
        queryset = Stock.objects.all().order_by('expirydate')

        if gtin is not None and shop is not None:
            queryset = queryset.filter(gtin=gtin)
            queryset = queryset.filter(shop=shop)
            queryset=queryset.first()

        serializer = StockSerializer(queryset)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status = 404)
