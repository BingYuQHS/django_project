from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.name