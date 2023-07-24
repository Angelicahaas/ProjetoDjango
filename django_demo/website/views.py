from django.shortcuts import render, redirect, get_object_or_404
from django.contrib .auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LogUsers, Bookform, ReviewForm
from .models import User, Book, Review


def home(request):
    user = User.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.success(request, "Tente novamente.")
    
    template = 'login.html' if request.path == '/login/' else 'home.html'
    return render(request, template)


def RegisterUser(request):
    form = LogUsers(request.POST or None)  # Cria o formulário com os dados do POST ou None
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Conta cadastrada com sucesso.")
            return redirect('login')
    # Se não for uma requisição POST, o formulário será passado para o template
    return render(request, 'registerusers.html', {'form': form})


def RegisterBooks(request):
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listbooks')

    else:
        form = Bookform()

    return render(request, 'registerbook.html', {'form': form})

    
def ListBooks(request):
    books = Book.objects.all()
    return render(request, 'listbooks.html', {'books': books})


reviews_db =[]
    
from .models import Review

def WriteReview(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            user = request.user

            # Certifique-se de que o usuário está autenticado antes de criar a revisão
            if user.is_authenticated:
                review = Review(book=book, user=user, rating=rating, comment=comment)
                review.save()
                return redirect('reviewupdate', review_id=review.id)

    else:
        form = ReviewForm()

    # Obtém todas as revisões salvas para esse livro
    reviews = Review.objects.filter(book=book)

    return render(request, 'writereview.html', {'form': form, 'book': book, 'reviews': reviews})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})



def ReviewUpdate(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book

    if request.method == 'POST':
        form = ReviewForm(request.POST or None, instance=review)
        if form.is_valid():
            form.save()

            # Salvar a revisão no dicionário
            review_data = {
                'book_id': book.id,
                'rating': form.cleaned_data['rating'],
                'comment': form.cleaned_data['comment'],
            }
            reviews_db[review_id] = review_data

            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviewupdate.html', {'form': form, 'book': book, 'review_id': review_id})


def ReviewDelete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    book = review.book

    if request.method == 'POST':
        review.delete()
        return redirect('book_detail', book_id=book.id)

    return render(request, 'reviewdelete.html', {'review': review, 'book': book})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('listbooks')
    
    return render(request, 'delete_book.html', {'book': book})