from django.shortcuts import render
from .serialalizers import ProductSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework import status


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderAdd(APIView):
    def post(self, request):
        order = OrderSerializer(data=request.data)

        if order.is_valid():
            order.save()
            return Response({'result': 'Пару секунд...'})

        return Response({'status': 'Ошибка'})

class ProductEdit(APIView):
    def put(self, request, *args, **kwargs):
        product_instance = Product.objects.filter(slug=kwargs['slug']).first()

        serializer = ProductSerializer(product_instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'result': 'Продукт успешно обновлён'}, status=status.HTTP_200_OK)
        
        return Response({'status': 'Ошибка', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)