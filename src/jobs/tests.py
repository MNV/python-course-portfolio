from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций выполненных работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="Job №1 image path",
            description="Job №1 description",
            full_description="Job №1 full description. " * 100,
        )

    def test_job_creation(self) -> None:
        """
        Тестирование моделей сообщений для выполненной работы.

        :return:
        """

        job = Job.objects.get(description="Job №1 description")

        content = "Job №1 full description. " * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
