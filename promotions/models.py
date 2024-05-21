from django.db import models
from products.models import Product
from cloudinary.models import CloudinaryField

class PromotionalPlayer(models.Model):
    image = CloudinaryField('image', blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    medals = models.TextField()
    product_to_promote = models.CharField(max_length=100)
    promotion_paragraph = models.TextField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
