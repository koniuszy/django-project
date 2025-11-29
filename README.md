# Django Project with REST Framework and Wagtail

A Django project demonstrating the integration of Django REST Framework and Wagtail CMS.

## Features

### Django REST Framework
- Example REST API with Book and Author models
- Full CRUD operations via ViewSets
- Browsable API interface
- Pagination support

### Wagtail CMS
- Home page with rich text content
- Blog pages with StreamField (headings, paragraphs, images, quotes, code blocks)
- Blog index page for listing posts
- Wagtail admin interface

## Project Structure

```
myproject/
├── api/                    # REST API app
│   ├── models.py          # Book and Author models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # ViewSets for API endpoints
│   └── urls.py            # API URL routing
├── home/                   # Wagtail home app
│   └── models.py          # HomePage, BlogPage, BlogIndexPage
├── myproject/             # Main project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # URL configuration
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── home/              # Wagtail page templates
└── requirements.txt       # Python dependencies
```

## Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## URLs

- **Home Page**: http://localhost:8000/
- **Wagtail Admin**: http://localhost:8000/admin/
- **Django Admin**: http://localhost:8000/django-admin/
- **REST API Root**: http://localhost:8000/api/
- **Books API**: http://localhost:8000/api/books/
- **Authors API**: http://localhost:8000/api/authors/

## API Endpoints

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book
- `GET /api/books/{id}/` - Retrieve a book
- `PUT /api/books/{id}/` - Update a book
- `PATCH /api/books/{id}/` - Partial update a book
- `DELETE /api/books/{id}/` - Delete a book

### Authors
- `GET /api/authors/` - List all authors
- `POST /api/authors/` - Create a new author
- `GET /api/authors/{id}/` - Retrieve an author
- `PUT /api/authors/{id}/` - Update an author
- `PATCH /api/authors/{id}/` - Partial update an author
- `DELETE /api/authors/{id}/` - Delete an author

## Wagtail Features

### Page Types

1. **HomePage**: Simple page with intro and body rich text fields
2. **BlogIndexPage**: Lists all child blog pages
3. **BlogPage**: Full blog post with StreamField support:
   - Headings
   - Rich text paragraphs
   - Image blocks
   - Quote blocks
   - Code snippets

### Creating Content

1. Log in to Wagtail admin at `/admin/`
2. Navigate to Pages
3. Create new pages using the available page types
4. Publish content to make it visible on the site

## Configuration

Environment variables:
- `DJANGO_SECRET_KEY`: Secret key for Django (default provided for development)
- `DJANGO_DEBUG`: Set to 'false' to disable debug mode
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `WAGTAILADMIN_BASE_URL`: Base URL for Wagtail admin links

## Development

Run tests:
```bash
python manage.py test
```

Run linting:
```bash
pip install flake8
flake8 api home myproject
```

