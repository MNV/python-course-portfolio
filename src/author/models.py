from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе.
    """

    skill_info = models.URLField(
        verbose_name="Резюме",
        help_text="Ссылка на резюме",
    )
    github_info = models.URLField(
        verbose_name="GitHub",
        help_text="Ссылка на github",
    )

    email_info = models.EmailField(
        verbose_name="Email",
        help_text="Email автора",
    )

    class Meta:
        verbose_name = "Данные об авторе"
        verbose_name_plural = "Данные об авторе"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'
