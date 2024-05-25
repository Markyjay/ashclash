from django.contrib.auth.models import User
from django.db import models

from products.models import Product

class Review(models.Model):
    """
    Model for a review on a product. The review is
    created by a user and includes a title, text,
    rating and helpful votes. A user must have ordered
    the product to create a review.
    """
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey( 
        User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
