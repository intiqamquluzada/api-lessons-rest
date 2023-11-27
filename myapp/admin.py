from django.contrib import admin
from myapp.models import Book, Category
# Register your models here.


admin.site.register(Book)
admin.site.register(Category)