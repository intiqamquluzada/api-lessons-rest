from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView)

from myapp.models import Book
from myapp.serializers import BookSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


