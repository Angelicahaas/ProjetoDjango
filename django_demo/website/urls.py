from django.urls import path
from . import views

urlpatterns = [
    path('',views.users, name='login'),
    path('registerusers/', views.RegisterUser, name='registeruser'),
    path('registerbooks/', views.RegisterBooks, name='registerbook'),
    path('writereview/', views.WriteReview, name='writereview'),
    path('reviewupdate/<int:pk>', views.ReviewUpdate, name='update'),
    path('reviewdelete/<int:pk>', views.ReviewDelete, name='delete'),a
]