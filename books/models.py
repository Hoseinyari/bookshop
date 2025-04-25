from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(unique=True)



class Book(models.Model):
    Book_title=models.CharField(max_length=255)
    Book_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Book_auther=models.CharField(max_length=255)
    Book_price=models.PositiveIntegerField