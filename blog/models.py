from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    post_date = models.DateField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
