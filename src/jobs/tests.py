from django.test import TestCase

from jobs.models import Job


class JobsTestCase(TestCase):
    """
    Тестирование функций блога.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            description="Job №1 description",
            content="Job №1 content. " * 100,
            image="Job №1 image path",
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей для работ.

        :return:
        """

        job = Job.objects.get(description="Job №1 description")

        content = "Job №1 content. " * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
