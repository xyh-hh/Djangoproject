from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .forms import BookForm


# class PublisherView(APIView):
#     """
#     获取所有出版社的信息
#     """
#     def get(self, request):
#         try:
#             publisher = Publisher.objects.all()
#             serializer = PublisherSerializer(publisher, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# 图书API
def book_list(request):
   books = Book.objects.all()
   response_text = "图书列表：\n"
   for book in books:
       response_text += f"{book.title}\t{book.author}\t{book.publisher}\n"
       return HttpResponse(response_text,content_type="text/plain")

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    detail_text = f"图书详情：\n"
    detail_text += f"ID: {book.id}\n"
    detail_text += f"标题: {book.title}\n"
    detail_text += f"作者: {book.author.name}\n"
    detail_text += f"出版社: {book.publisher.name}\n"
    detail_text += f"ISBN: {book.isbn}\n"
    return HttpResponse(detail_text, content_type='text/plain')
@csrf_exempt
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return HttpResponse(f"图书创建成功: {book.title}(ID:{book.id})", status=201, content_type='text/plain')
        return HttpResponse(f"图书创建失败: {form.errors}", status=400, content_type='text/plain')
    return HttpResponse("请使用POST请求创建图书", status=405, content_type='text/plain')
@csrf_exempt
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return HttpResponse(f"图书更新成功：{book.title}(ID:{book.id})", status=201, content_type='text/plain')
        return HttpResponse(f"图书更新失败{form.errors}", status=400, content_type='text/plain')
    return HttpResponse("请使用POST请求更新图书", status=405, content_type='text/plain')

@csrf_exempt
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return HttpResponse(f"图书删除成功: {book.title}", content_type='text/plain')
    return HttpResponse(f"请使用POST请求删除图书", status=405, content_type='text/plain')

# 作者视图
# def author_list(request):
#     return render(request, 'library/author_list.html', {'authors': Author.objects.all()})
#
# def author_detail(request, pk):
#     return render(request, 'library/author_detail.html', {'author': get_object_or_404(Author, pk=pk)})
#
# def author_create(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             return redirect(form.save().get_absolute_url())
#     else:
#         form = AuthorForm()
#     return render(request, 'library/author_form.html', {'form': form})
#
# def author_update(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'POST':
#         form = AuthorForm(request.POST, instance=author)
#         if form.is_valid():
#             return redirect(form.save().get_absolute_url())
#     else:
#         form = AuthorForm(instance=author)
#     return render(request, 'library/author_form.html', {'form': form, 'author': author})
#
# def author_delete(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'POST':
#         author.delete()
#         return redirect('author-list')
#     return render(request, 'library/author_delete.html', {'author': author})
#
# # 出版社视图
# def publisher_list(request):
#     return render(request, 'library/publisher_list.html', {'publishers': Publisher.objects.all()})
#
# def publisher_detail(request, pk):
#     return render(request, 'library/publisher_detail.html', {'publisher': get_object_or_404(Publisher, pk=pk)})
#
# def publisher_create(request):
#     if request.method == 'POST':
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             return redirect(form.save().get_absolute_url())
#     else:
#         form = PublisherForm()
#     return render(request, 'library/publisher_form.html', {'form': form})
#
# def publisher_update(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == 'POST':
#         form = PublisherForm(request.POST, instance=publisher)
#         if form.is_valid():
#             return redirect(form.save().get_absolute_url())
#     else:
#         form = PublisherForm(instance=publisher)
#     return render(request, 'library/publisher_form.html', {'form': form, 'publisher': publisher})
#
# def publisher_delete(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     if request.method == 'POST':
#         publisher.delete()
#         return redirect('publisher-list')
#     return render(request, 'library/publisher_delete.html', {'publisher': publisher})
