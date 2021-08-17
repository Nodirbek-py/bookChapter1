from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    name = models.CharField(max_length=128, help_text="Name of the publisher")
    website = models.URLField(help_text="Publisher's website")
    email = models.EmailField(help_text="Email of the publisher")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="First name of the author")
    last_name = models.CharField(max_length=64, verbose_name="Last name of the author")
    email = models.EmailField(verbose_name="Email of the author")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title of the book")
    publication_date = models.DateField(auto_now=True, verbose_name="Publication date of the book")
    isbn = models.CharField(max_length=20, verbose_name="ISBN of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_DEFAULT, default=1)
    contributors = models.ManyToManyField(Author, through="BookContributor")

    def __str__(self):
        return self.title





class BookContributor(models.Model):
    roles = (
        ('Author', 'author'),
        ('CO-Author', 'co-author'),
        ('Editor', 'editor')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Author, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",choices=roles, max_length=20)



class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
