
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from review.forms import ReviewForm
from django.core.mail import send_mail
from MyShelf.settings import DEFAULT_FROM_EMAIL
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

            title = f"Thank you for your review on the book {book.title} by {book.author}."
            content = f"Hello {request.user.get_full_name()}, thank you for reviewing {book.title} with {review.rating} ⭐!\n"\
                      f"You also left a comment that says: - {review.comment}\n"\
                      f"\nBest regards, MyShelf Team! ❤︎⁠"
                      
            send_mail(
                subject = title,
                message= content,
                from_email = DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False
            )


    
            return redirect('list-books-per-category', book.category.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review/add_review.html', {'book': book, 'form': form})