from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_of_creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title