from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_date', 'email']


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date',
                  'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class BookListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing books."""

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn']
