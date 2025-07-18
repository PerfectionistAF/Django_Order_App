from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from products.models import Product, Order, OrderItem
from products.serializers import ProductSerializer, OrderSerializer


##view restapi for products
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(company=self.request.user.company, is_active=True)
    
class ProductDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        ids = request.data.get('ids', [])
        Product.objects.filter(id__in=ids, company=request.user.company).update(is_active=False)
        return Response("Products deleted successfully")

class OrderCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]  
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(
            company=self.request.user.company,
            created_by=self.request.user
        )


class OrderListView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create_operation(self, serializer):
        serializer.save(company=self.request.user.company,
                        created_at=self.request.timestamp,
                        last_updated_at=self.request.timestamp)