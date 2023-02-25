"""
Функции панели управления для приложения "Выполненные работы".
"""

from django.contrib import admin

from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "image",
        "created_at",
        "updated_at",
    )

    search_fields = ("description", "content")

    list_filter = (
        "created_at",
        "updated_at",
    )
