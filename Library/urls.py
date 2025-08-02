from django.urls import path #应用
from . import views  # 导入当前应用的视图模块

urlpatterns = [
    # 图书相关URL
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('books/new/', views.book_create, name='book-create'),
    path('books/<int:pk>/edit/', views.book_update, name='book-update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book-delete'),

    # 作者相关URL
    path('authors/', views.author_list, name='author-list'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    path('authors/new/', views.author_create, name='author-create'),
    path('authors/<int:pk>/edit/', views.author_update, name='author-update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author-delete'),

    # 出版社相关URL
    path('all_publisher/',views.PublisherView.as_view(), name='获取所有出版社信息'),
    path('publishers/', views.publisher_list, name='publisher-list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher-detail'),
    path('publishers/new/', views.publisher_create, name='publisher-create'),
    path('publishers/<int:pk>/edit/', views.publisher_update, name='publisher-update'),
    path('publishers/<int:pk>/delete/', views.publisher_delete, name='publisher-delete'),
]
