from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=255,unique=True)
    cat_slug = models.SlugField() 



class Book(models.Model):
    Book_title = models.CharField(max_length=255)
    book_image = models.ImageField()
    book_slug = models.SlugField(max_length=100, unique=True)
    Book_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Book_auther = models.CharField(max_length=255)
    Book_price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.Book_title
    