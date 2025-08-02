from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm
from .ser.pub_ser import PublisherSerializer


class PublisherView(APIView):
    """
    获取所有出版社的信息
    """
    def get(self, request):
        try:
            publisher = Publisher.objects.all()
            serializer = PublisherSerializer(publisher, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 图书视图
def book_list(request):
    return render(request, 'library/book_list.html', {'books': Book.objects.all()})

def book_detail(request, pk):
    return render(request, 'library/book_detail.html', {'book': get_object_or_404(Book, pk=pk)})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'library/book_delete.html', {'book': book})

# 作者视图
def author_list(request):
    return render(request, 'library/author_list.html', {'authors': Author.objects.all()})

def author_detail(request, pk):
    return render(request, 'library/author_detail.html', {'author': get_object_or_404(Author, pk=pk)})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = AuthorForm()
    return render(request, 'library/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/author_form.html', {'form': form, 'author': author})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author-list')
    return render(request, 'library/author_delete.html', {'author': author})

# 出版社视图
def publisher_list(request):
    return render(request, 'library/publisher_list.html', {'publishers': Publisher.objects.all()})

def publisher_detail(request, pk):
    return render(request, 'library/publisher_detail.html', {'publisher': get_object_or_404(Publisher, pk=pk)})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = PublisherForm()
    return render(request, 'library/publisher_form.html', {'form': form})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            return redirect(form.save().get_absolute_url())
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'library/publisher_form.html', {'form': form, 'publisher': publisher})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher-list')
    return render(request, 'library/publisher_delete.html', {'publisher': publisher})
