from django.db import models
from django.utils.text import slugify
# Create your models here.

categories = {
    "fiction":"تخیلی" ,
    "non-fiction":"داستان واقعی",
    "biography":"بیوگرافی",
    "science":"علمی",
    "history":"تاریخی",
    "fantasy":"فانتزی",
    "romance":"رومانتیک",
    "mystery":"رازالود",
    "children":"مناسب کودکان",
    "other":"موضوعات دیگر"
    }



class Book(models.Model):
    Book_title = models.CharField(max_length=255)
    book_image = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True)
    Book_category = models.CharField(max_length=255,choices =categories)
    Book_auther = models.CharField(max_length=255)
    Book_price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Book_title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.Book_title
    