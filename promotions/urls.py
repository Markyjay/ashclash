from django.urls import path
from .views import promotional_page

urlpatterns = [
    path('', promotional_page, name='promotional_page'),
]