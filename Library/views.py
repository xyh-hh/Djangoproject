from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Publisher
from .serializers import BookSerializer, PublisherSerializer


class BookListView(APIView):
    """获取所有图书的列表信息"""
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookCreateView(APIView):
    """创建新的图书"""
    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    """获取指定ID的图书详情"""
    def get(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookUpdateView(APIView):
    """更新指定ID的图书信息"""
    def post(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    """删除指定ID的图书记录"""
    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PublisherView(APIView):
    """获取所有出版社的信息"""
    def get(self, request):
        try:
            publishers = Publisher.objects.all()  # 变量名修正（复数形式更合理）
            serializer = PublisherSerializer(publishers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)