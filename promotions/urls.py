from django.urls import path
from products.views import product_detail
from .views import promotional_page

urlpatterns = [
    path('promotions/', promotional_page, name='promotional_page'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
