from django.shortcuts import render, redirect
from .models import Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm

def index(request):
    return render(request, 'myapp/index.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'myapp/form.html', {'form': form})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'myapp/form.html', {'form': form})

def create_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PublisherForm()
    return render(request, 'myapp/form.html', {'form': form})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
            return render(request, 'myapp/search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'myapp/search.html', {'form': form})