from django.contrib import admin
from .models import Book

# Register your models here.
# Registering your database here will add the database to Django Administration
admin.site.register(Book)
