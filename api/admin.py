from django.contrib import admin

from api.models import Snippet


class adminSnippet(admin.ModelAdmin):
    list_display = ("title", "language", "created")
    search_fields = ("title", "code")


admin.site.register(Snippet, adminSnippet)
