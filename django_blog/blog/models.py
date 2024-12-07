from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current timestamp when created
    author = models.ForeignKey(
        User,  # Reference to Django's built-in User model
        on_delete=models.CASCADE,  # Delete all posts by the user if the user is deleted
        related_name='posts'  # Allows reverse lookup like user.posts.all()
    )

    def __str__(self):
        return self.title  # String representation of the post, displays the title

