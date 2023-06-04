from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    desc = models.TextField()
    book_id = models.AutoField(primary_key=True)
