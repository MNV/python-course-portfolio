# Generated by Django 4.1.7 on 2023-02-25 12:45

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Содержимое сообщения"
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="images/", verbose_name="Изображение"),
                ),
                (
                    "publication_date",
                    models.DateTimeField(verbose_name="Дата публикации"),
                ),
            ],
            options={
                "verbose_name": "Сообщение блога",
                "verbose_name_plural": "Сообщения блога",
            },
        ),
    ]
