from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций выполненной работы.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            full_description="РАБОТА" * 10,
            image="РАБОТА КАРТИНКА",
            description="РАБОТА ОПИСАНИЕ",
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для выполненной работы.

        :return:
        """

        job = Job.objects.get(description="РАБОТА ОПИСАНИЕ")

        full_description = "РАБОТА" * 10
        self.assertEqual(job.summary(), full_description[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')