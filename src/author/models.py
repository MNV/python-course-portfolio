from django.db import models
from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения информации об авторе.
    """

    cv_link = models.URLField(verbose_name="Ссылка на резюме")
    github_link = models.URLField(verbose_name="Ссылка на GitHub")
    email = models.EmailField(verbose_name="Почтовый адрес")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f'Объект "автор" (id={self.pk})'
