from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "skill_info",
        "github_info",
        "email_info",
        "created_at",
        "updated_at",
    )

    search_fields = ("email",)

    list_filter = (
        "created_at",
        "updated_at",
    )
