from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Book

# Create your views here.

from django.shortcuts import render 
from django.http import HttpResponseRedirect
from transitions.models import Transition
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here. 

#نمایش تمام کتاب ها در صفحه اصلی
@login_required
def home_view(request): 
    all_books = Book.objects.all()
    return render(request,'books/home.html',{"all_books": list(all_books)})
def book_detail(request):
    the_book = Book.objects.get(book_slug = book_slug)
@login_required
#نمایش درامد ها
def income_view(request): 
    incomes = Transition.objects.filter(category = 'income')
    return render(request,'transitions/income.html', {"incomes": list(incomes)}) 