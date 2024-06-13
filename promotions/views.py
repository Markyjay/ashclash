from django.shortcuts import render
from .models import PromotionalPlayer


def promotional_page(request):
    players = PromotionalPlayer.objects.all()
    context = {
        'players': players,
    }
    return render(
        request, 'promotions/promotions.html', context)


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
    return render(request, 'promotions/edit_promotion.html', context)


def delete_promotion(request, pk):
    player = get_object_or_404(PromotionalPlayer, pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Promotion deleted successfully.')
        return redirect('promotional_page')
    context = {
        'player': player,
    }
    return render(request, 'promotions/delete_promotion.html', context)