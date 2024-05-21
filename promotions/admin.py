from django.contrib import admin
from .models import PromotionalPlayer
from cloudinary.models import CloudinaryField

class PromotionalPlayerAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'image_url',
        'name',
        'age',
        'team',
        'medals',
        'promotion_paragraph',
        'product',
    )

admin.site.register(PromotionalPlayer, PromotionalPlayerAdmin)


