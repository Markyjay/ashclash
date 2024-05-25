from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.list_reviews, name='reviews'),
    path('add/<int:product_id>/', views.create_review, name='create_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]