from django.contrib import admin
from .models import Book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
  list_display = ("title", "category", "auther","price")
  slug = {"slug": ("title", "auther")}
  
admin.site.register(Book, bookAdmin)