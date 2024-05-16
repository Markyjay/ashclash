from django.db import models


class PromotionalPlayer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    medals = models.TextField()
    product_to_promote = models.CharField(max_length=100)
    promotion_paragraph = models.TextField()

    def __str__(self):
        return self.name
