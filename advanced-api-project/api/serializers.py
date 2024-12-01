from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Handles validation and serialization of Book data.
    """

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
        # 'fields' defines the fields that will be included in the serialized output.

    def validate(self, data):
        """
        Validates the Book data.
        
        Ensures the `publication_year` is not in the future.
        This method is called automatically during serializer validation.
        """
        if data['publication_year'] > timezone.now().year:  # Compare with the current year
            raise serializers.ValidationError("Publication year cannot be in the future!")
        return data  # If validation passes, return the validated data


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes nested serialization for the related books.
    """

    # Serialize the related books (reverse relationship to the Book model).
    # Using 'many=True' because an author can have multiple books.
    # 'read_only=True' ensures that the books cannot be directly created/updated via this serializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
        # 'fields' defines the fields that will be included in the serialized output.

    """
    Notes:
    - The `books` field relies on the reverse relationship defined in the Book model.
      Ensure the `Book` model's foreign key to `Author` uses `related_name='books'`
      or leave it as default (Django will use the lowercase name of the model, i.e., 'book').
    """
