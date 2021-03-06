# from tkinter import CASCADE
from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='book_author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name='book_publisher', null=True)

    def __str__(self):
        return self.title
