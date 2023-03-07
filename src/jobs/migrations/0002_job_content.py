# Generated by Django 4.1.7 on 2023-03-03 13:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                default="", verbose_name="Подробное описание работы"
            ),
        ),
    ]
