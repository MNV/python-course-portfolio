# Create your models here.

from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе.
    """

    resume_url = models.URLField(
        verbose_name="Резюме",
        help_text="Ссылка на резюме автора",
    )
    github_url = models.URLField(
        verbose_name="GitHub",
        help_text="Ссылка на гитхаб автора",
    )

    email = models.EmailField(
        verbose_name="Почта",
        help_text="Почта автора",
    )

    class Meta:
        verbose_name = "Данные об авторе"
        verbose_name_plural = "Данные об авторе"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'
