from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'myapp/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html', {'book': book})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        price = request.POST.get('price', )
        bookimage = request.FILES['bookimage']

        book = Book(name=name, description=description, price=price, bookimage=bookimage)
        book.save()
    return render(request, 'myapp/add_book.html')


def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'myapp/edit.html', {'form': form, 'book': book})


def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
