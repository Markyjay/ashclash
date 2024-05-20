from django.shortcuts import render
from .models import PromotionalPlayer


def promotional_page(request):
    players = PromotionalPlayer.objects.all()
    return render(
        request, 'promotions/promotions.html', {'players': players})
