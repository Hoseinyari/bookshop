from django.db import models
# Create your models here.

class Category(models.Model):
    cat_slug = models.SlugField(max_length=200)
    cat_name = models.CharField(max_length=200,unique=True)


class Book(models.Model):
    book_id=models.IntegerField(unique=True, primary_key=True, default=00000)
    Book_title = models.CharField(max_length=255)
    Book_description = models.TextField(null=True)
    Book_auther = models.CharField(max_length=255)
    Book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Book_price = models.PositiveIntegerField()
    Book_slug = models.SlugField(max_length=500, unique=True)

class book_image():
    book_id=models.ForeignKey(Book , on_delete=models.CASCADE)
    book_image = models.ImageField(default="defaul.jpg", upload_to="books/photos/")
    
class BookDto:

    def __init__(self,book:Book):
        self.book : Book = book
        self.image  = None
    