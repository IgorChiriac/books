from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
import datetime

class Book(models.Model):
  id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
  title = models.CharField(max_length=200)
  authors = models.ManyToManyField('Author', blank=False)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  cover = models.ImageField(upload_to='covers/', blank=True)

  class Meta:
    indexes = [
      models.Index(fields=['id'], name='id_index'),
    ]
    permissions = [
      ('read_all_books', 'Can read all books'),
    ]

  def __str__(self): 
    return self.title

  def get_absolute_url(self):
    return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
  book = models.ForeignKey(
    Book,
    on_delete=models.CASCADE,
    related_name='reviews',
  )
  review = models.CharField(max_length=255)
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.review

class Author(models.Model):
  id = models.UUIDField(
      primary_key=True,
      default=uuid.uuid4,
      editable=False)
  books = models.ManyToManyField(Book, blank=True, related_name='author_book')
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  birthday=models.DateField(auto_now=False, null=True, blank=True)
  website = models.CharField(max_length=200)
  biography = models.TextField()

  @property
  def full_name(self):
    "Returns the authors's full name."
    return '%s %s' % (self.first_name, self.last_name)
  
  @property
  def age(self):
    "Returns the authors's age."
    if self.birthday:
      today = datetime.date.today()
      return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
    else:
      return None

  def __str__(self):
    return self.first_name+" "+self.last_name
