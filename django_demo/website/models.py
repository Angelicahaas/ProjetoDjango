from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return(f"Usuário {self.nome} cadastrado.")
    


class Book(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    author = models.CharField(verbose_name="Autor", max_length=100)
    publication_date = models.DateField(verbose_name="Data de Publicação")
    
    def __str__(self):
        return self.title
    


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    coment = models.CharField(verbose_name="comentário.", max_length=100)

    
    def __str__(self):
        return self.coment