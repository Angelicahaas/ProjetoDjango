from django.shortcuts import render, redirect, get_object_or_404
from django.contrib .auth import authenticate, login
from django.contrib import messages
from .forms import LogUsers, Bookform, ReviewForm
from .models import User, Book, Review


def home(request):
    user = User.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('users')
        else:
            messages.success(request, "Tente novamente.")
            return redirect('users')
    
    else: 
        return render(request, 'login.html', {'user': user})
    

def RegisterUser(request):
    if request.method == 'POST':
        form = LogUsers(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Conta cadastrada com sucesso.")
            return redirect('users')
        else:
            form = LogUsers()
            return render(request, 'registeruser.html', {'form': form})
        



def RegisterBooks(request):
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form = Bookform()

        return render(request, 'registerbook.html', {'form': form})
    
    
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
        
        return render(request, 'writereview.html', {'form': form, 'book': book})
    
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

    return render(request, 'reviewupdate.html', {'form': form, 'book': book})

def ReviewDelete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book

    if request.method == 'POST':
        review.delete()
        return redirect('book_detail', book_id=book.id)

    return render(request, 'reviewdelete.html', {'review': review, 'book': book})