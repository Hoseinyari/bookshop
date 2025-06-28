from django.contrib import admin
from .models import Book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
  list_display = ("book_id","Book_title", "Book_category","Book_description", "Book_auther","Book_price")
#  slug = {"slug": ("title", "auther")}
  
admin.site.register(Book, bookAdmin)
