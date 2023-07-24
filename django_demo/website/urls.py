from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.home, name='login'),
    path('registerusers/', views.RegisterUser, name='registerusers'),
    path('registerbooks/', views.RegisterBooks, name='registerbook'),
    path('listbooks/', views.ListBooks, name='listbooks'),
    path('bookdetail/<int:book_id>/', views.book_detail, name='bookdetail'),
    path('bookdelete/<int:book_id>/', views.delete_book, name='deletebook'),
    path('writereview/<int:book_id>', views.WriteReview, name='writereview'),
    path('reviewupdate/<int:review_id>', views.ReviewUpdate, name='reviewupdate'),
    path('reviewdelete/<int:pk>', views.ReviewDelete, name='reviewdelete'),
    path('review/<int:book_id>/', views.Review, name='review'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]