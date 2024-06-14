from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import PromotionalPlayer
from .forms import PromotionalPlayerForm

def promotional_page(request):
    players = PromotionalPlayer.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'promotions/promotions.html', context)

def create_promotion(request):
    if request.method == 'POST':
        form = PromotionalPlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promotion created successfully.')
            return redirect('promotional_page')
    else:
        form = PromotionalPlayerForm()
    context = {
        'form': form,
    }
    return render(request, 'promotions/create_promotions.html', context)

def edit_promotion(request, pk):
    player = get_object_or_404(PromotionalPlayer, pk=pk)
    if request.method == 'POST':
        form = PromotionalPlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promotion updated successfully.')
            return redirect('promotional_page')
    else:
        form = PromotionalPlayerForm(instance=player)
    context = {
        'form': form,
        'player': player,
    }
    return render(request, 'promotions/edit_promotions.html', context)

def delete_promotion(request, pk):
    player = get_object_or_404(PromotionalPlayer, pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Promotion deleted successfully.')
        return redirect('promotional_page')
    context = {
        'player': player,
    }
    return render(request, 'promotions/delete_promotions.html', context)