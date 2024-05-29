from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Review
from products.models import Product
from checkout.models import Order, OrderLineItem
from .forms import ReviewForm


def list_reviews(request):
    """View to list all reviews."""
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'review/reviews.html', context)

@login_required
def create_review(request, product_id):
    """
    View to create a review on a product page. The
    review is created using the form data and saved
    to the database. It can only be created by a user
    who is logged in and has purchased the product.
    """
    product = Product.objects.get(id=product_id)

    if not OrderLineItem.objects.filter(order__user_profile=request.user.userprofile, product=product).exists():
        messages.error(
            request, "You must have purchased this product to review it.")
        print (messages.error)
        return redirect('product_detail', product_id)
    else:
        pass
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
    """
    View to edit a review. The review is retrieved
    from the database and the form is pre-populated
    with the review data. The review is then updated
    and saved to the database.
    """
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
    """
    View to delete a review. The review is retrieved
    from the database and then deleted.
    """
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        raise PermissionDenied("You can only delete your own reviews.")
    
    review.delete()
    messages.success(request, "Your review has been deleted.")
    return redirect('product_detail', product_id=review.product.id)
