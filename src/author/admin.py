from django.contrib import admin

# Register your models here.
from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "resume_url",
        "github_url",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = ("email",)

    list_filter = (
        "created_at",
        "updated_at",
    )