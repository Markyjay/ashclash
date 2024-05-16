from django.shortcuts import render
from .models import PromotionalPlayer


def promotional_page(request):
    players = PromotionalPlayer.objects.all()
    return render(
        request, 'promotions/promotional_page.html', {'players': players})
