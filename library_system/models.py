from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    copies_available = models.IntegerField()


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    borrowed_books = models.ManyToManyField(Book, through="Borrowing")


class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_on = models.DateField(verbose_name=_("borrowed date"))
    due_date = models.DateField(verbose_name=_("due date"))
    renewed = models.BooleanField(default=False)
    borrowed_status = models.BooleanField(default=False)
    returned_status = models.BooleanField(default=False)
    # Add a new field to track the number of times the book has been renewed.
    renewed_count = models.IntegerField(default=0)
