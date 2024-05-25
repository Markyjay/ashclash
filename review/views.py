from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Review
from products.models import Product

from .forms import ReviewForm


def list_reviews(request):
    """ """
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

    form = ReviewForm()

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review = Review(
            product=product,
            title=title,
            text=text,
            rating=rating
        )
        review.save()

        messages.success(request, "Your review has been added.")
        return redirect('product_detail', product_id)

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
    review = Review.objects.get(id=review_id)
    product = review.product
    form = ReviewForm(initial={
        'title': review.title,
        'text': review.text,
        'rating': review.rating
    })

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        rating = request.POST['rating']
        review.title = title
        review.text = text
        review.rating = rating
        review.save()

        messages.success(request, "Your review has been updated.")
        return redirect('product_detail', product.id)

    context = {
        'product': product,
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
    review = Review.objects.get(id=review_id)
    product = review.product
    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('product_detail', product.id)
