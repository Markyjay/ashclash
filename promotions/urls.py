from django.urls import path
from .views import promotional_page

urlpatterns = [
    path('promotions/', promotional_page, name='promotional_page'),
]
