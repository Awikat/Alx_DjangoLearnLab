from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Author model
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensures unique author names

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',  # Allows accessing books by an author via `author.books.all()`
    )
    publication_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book_per_author'),
        ]  # Ensures a book with the same title cannot be assigned to the same author

    def __str__(self):
        return self.title


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Email is the unique identifier
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Use email for authentication instead of username
    REQUIRED_FIELDS = ['username']  # Username is still required but not for authentication

    def __str__(self):
        return self.email
