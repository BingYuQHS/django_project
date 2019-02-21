from django.db import models

# Create your models here.
class Book(models.Model):
    objects = models.Manager()
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
