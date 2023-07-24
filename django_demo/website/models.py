from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("O email deve ser fornecido")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # Verifica se o objeto já existe no banco de dados (update) ou é novo (create)
        if not self.pk:  # Novo objeto (create)
            # Definir a senha correta para o novo usuário aqui
            self.set_password('senha_correta')
        # Chama o método save() original para salvar o objeto no banco de dados
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"Usuário {self.name} cadastrado."

class Book(models.Model):
    GENDER_CHOICES = (
        ('Fiction', 'Ficção'),
        ('Non-fiction', 'Não Ficção'),
        ('Mystery', 'Mistério'),
        ('Romance', 'Romance'),
        ('Thriller', 'Suspense'),
        ('Fantasy', 'Fantasia'),
        ('Science Fiction', 'Ficção Científica'),
        ('Horror', 'Terror'),
        ('Biography', 'Biografia'),
        ('Self-Help', 'Autoajuda'),
        ('History', 'História'),
        ('Poetry', 'Poesia'),
        ('Comics', 'Histórias em Quadrinhos'),
        ('Cooking', 'Culinária'),
        ('Travel', 'Viagens'),
        ('Health', 'Saúde'),
        ('Others', 'Outros'),
    )

    title = models.CharField(verbose_name="Título", max_length=100)
    author = models.CharField(verbose_name="Autor", max_length=100)
    gender = models.CharField(
        verbose_name="Gênero",
        max_length=100, 
        choices=GENDER_CHOICES,
        default='F'
          
    )

    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.CharField(verbose_name="comentário.", max_length=100)

    def __str__(self):
        return self.comment
