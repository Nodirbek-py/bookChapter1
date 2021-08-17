from django.shortcuts import render
from .models import Book


def search(request):
    query = request.GET["query"]
    books = Book.objects.all()
    data = []
    for book in books:
        print(query in book.title)
        print(book.title)
        if query in book.title:
            data.append(book)
            
    return render(request, "search-book.html", {'data': data})