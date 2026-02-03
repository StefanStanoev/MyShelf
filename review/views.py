
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from review.forms import ReviewForm
from book.models import Book
from review.models import Review


@login_required
def add_review(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    try:
        review = Review.objects.get(book=book, user=request.user)
    except Review.DoesNotExist:
        review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review=form.save(commit=False)
            review.book = book
            review.user = request.user
            form.save()
    
            return redirect('list-books-per-category', book.category.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review/add_review.html', {'book': book, 'form': form})