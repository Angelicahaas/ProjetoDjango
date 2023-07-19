from django.shortcuts import render, redirect, get_object_or_404
from .forms import Bookform, ReviewForm
from .models import Book, Review


def RegisterBooks(request):
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form = Bookform()

        return render(request, 'register_bool.html', {'form': form})
    
def WriteReview(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            user = request.user

            review = Review(book=book, user=user, rating=rating, comment=comment)
            review.save()
            return redirect('book_detail', book_id=book.id)
        else:
            form = ReviewForm
        
        return render(request, 'WriteReview.html', {'form': form, 'book': book})
    
def ReviewUpdate(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review_update.html', {'form': form, 'book': book})

def ReviewDelete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book

    if request.method == 'POST':
        review.delete()
        return redirect('book_detail', book_id=book.id)

    return render(request, 'review_delete.html', {'review': review, 'book': book})