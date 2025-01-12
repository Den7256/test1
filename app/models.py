from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    GENGE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NON', 'Non-Fiction'),
        ('SCI', 'Sciencee Fiction'),
        ('FAN', 'Fantasy'),
        ('MYS', 'Mystery')
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    genre = models.CharField(
        max_length=3,
        choices=GENGE_CHOICES,
        default='FIC'
    )
    def __str__(self):
        return self.title

