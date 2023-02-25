from django.test import TestCase

from author.models import Author


class JobTestCase(TestCase):
    """
    Тестирование функций работы
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.
        :return:
        """

        Author.objects.create(
            resume_url="https://test.test",
            github_url="https://test.test",
            email="test@test.test",
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей работы.
        :return:
        """

        author = Author.objects.get(resume_url="https://test.test")
        self.assertEqual(author.github_url, "https://test.test")
        self.assertEqual(author.email, "test@test.test")
        self.assertEqual(str(author), f'Объект "Автор" (id={author.pk})')
