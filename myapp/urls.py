from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", BookListView.as_view(), name='book-list'),
    path("book/<id>/", BookDetailView.as_view(), name='book-detail'),
    path("update/<id>/", BookUpdateView.as_view(), name='update'),
]