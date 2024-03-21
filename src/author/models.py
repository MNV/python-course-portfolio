from django.db import models
from base.models import TimeStampMixin


class Author(TimeStampMixin):
    resume = models.URLField(verbose_name="Ссылка на резюме")
    github = models.URLField(verbose_name="Ссылка GitHub")
    email = models.EmailField(verbose_name="Email автора")

    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "автор" (id={self.pk})'