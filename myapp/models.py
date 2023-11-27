from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name="Category name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Book name")
    page_count = models.CharField(max_length=255, verbose_name="Count of page")
    author = models.CharField(max_length=255, verbose_name="Author of book")
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Book"
        verbose_name_plural = "Books"
