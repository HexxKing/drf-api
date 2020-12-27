from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Book

class BookModelTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    test_user = get_user_model().objects.create_user(username='tester', password='pass')
    test_user.save()

    test_book = Book.objects.create(
      author = test_user,
      title = 'Title of Book'
      subtitle = "Subtitle of Book"
    )
    test_book.save()

  def test_book_content(self):
    book = Book.objects.get(id=1)

    self.assertEqual(str(book.author), 'tester')
    self.assertEqual(book.title, 'Title of Book')
    self.assertEqual(book.subtitle, 'Subtitle of Book')


