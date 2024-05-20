from django.contrib import admin

from .models import PromotionalPlayer

class PromotionalPlayer(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'age',
        'team',
        'medals',
        'promotion_paragraph',
        'product',
    )

admin.site.register(Product, ProductAdmin)