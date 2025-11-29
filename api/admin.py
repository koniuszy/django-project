from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'author', 'isbn']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birth_date']
    search_fields = ['name', 'email']
