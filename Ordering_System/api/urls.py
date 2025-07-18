from django.urls import path
from .views import OrderCreateView, ProductListView, ProductDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
]