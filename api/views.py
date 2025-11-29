from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Book, Author
from .serializers import BookSerializer, BookListSerializer, AuthorSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """API root endpoint showing available endpoints."""
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'authors': reverse('author-list', request=request, format=format),
    })


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing books.

    Provides list, create, retrieve, update, partial_update, and destroy actions.

    list:
        Return a list of all books.

    create:
        Create a new book.

    retrieve:
        Return the given book.

    update:
        Update a book.

    partial_update:
        Partially update a book.

    destroy:
        Delete a book.
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing authors.

    Provides CRUD operations for author records.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
