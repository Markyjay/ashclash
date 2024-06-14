from django.urls import path
from products.views import product_detail
from .views import promotional_page, create_promotion, edit_promotion, delete_promotion

urlpatterns = [
    path('promotions/', promotional_page, name='promotional_page'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('promotions/create/', create_promotion, name='create_promotion'),
    path('promotions/edit/<int:pk>/', edit_promotion, name='edit_promotion'),
    path('promotions/delete/<int:pk>/', delete_promotion, name='delete_promotion'),
]
