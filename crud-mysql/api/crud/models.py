from django.db import models


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    type = models.CharField(
        max_length=100, choices=(("Fiction", "Fiction"), ("Non Fiction", "Non Fiction"))
    )
    added_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    books = models.ForeignKey(Books, models.CASCADE)
