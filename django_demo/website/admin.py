from django.contrib import admin
from .models import Book, Review

# Register your models here.

Book.site.register(Book)
Review.site.register(Review)
