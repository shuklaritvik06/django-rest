from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_desc = models.CharField(max_length=200)
    book_isbn = models.CharField(max_length=25)
    