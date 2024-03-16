"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin
from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "cv_link",
        "github_link",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = ("email", "github_link")

    list_filter = (
        "created_at",
        "updated_at",
    )
