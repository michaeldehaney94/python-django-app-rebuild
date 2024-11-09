from django.db import models


# Create your models here.
class Book(models.Model):

    # To view the record name entered in specific object while using Django ORM shell
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)  # book name
    description = models.CharField(max_length=300)  # book description
    price = models.IntegerField()
    bookimage = models.ImageField(default='default.jpg', upload_to='book_images/')  # store book cover image
