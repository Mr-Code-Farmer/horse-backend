from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    release_year =models.IntegerField()

    #if you print a book, this will return a string version of it's title
    def __str__(self):
        return self.title
