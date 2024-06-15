from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Review
from products.models import Product
from checkout.models import OrderLineItem
from .forms import ReviewForm


def list_reviews(request):
    """View to list all reviews."""
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'review/reviews.html', context)

def create_review(request, product_id):
    """View to create a review."""
    product = get_object_or_404(Product, id=product_id)
    if not OrderLineItem.objects.filter(order__user_profile=request.user.userprofile, product=product).exists():
        messages.error(request, "You must have purchased this product to review it.")
        return redirect('product_detail', product_id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, "Your review has been added.")
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'review/create_review.html', context)

@login_required
def edit_review(request, review_id):
    """View to edit a review."""
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise PermissionDenied("You can only edit your own reviews.")
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated.")
            return redirect('product_detail', product_id=review.product.id)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'review/edit_review.html', context)

@login_required
def delete_review(request, review_id):
    """View to delete a review."""
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise PermissionDenied("You can only delete your own reviews.")
    if request.method == 'POST':
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect('product_detail', product_id=review.product.id)
    context = {
        'review': review,
    }
    return render(request, 'review/delete_review.html', context)