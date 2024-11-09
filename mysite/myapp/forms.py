# this function class inherits the book model fields to create and reuse and render a single form template for
# creating forms for editing data or adding data in webpages.

from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'bookimage']
