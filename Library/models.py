from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    class Meta:
       ordering = ['name']

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,related_name='books')
    isbn = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']

# Create your models here.
