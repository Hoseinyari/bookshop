from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from books.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request): 
# if you did not select categoty
    cats = books.objects.all()
    images = list()
    if cats is None:
        books = Book.objects.all()
        return render(request,'books/home.html',{'cats': cats})
    else:

        selected_cat = request.GET.get('Book_category')
        books = Book.objects.filter(Book_category=selected_cat)
        return render(request, 'books/home.html',{'cats': cats, "current_cat": cats})

#نمایش جزببات یک کناب

def book_detail(request,book_id):
    the_book = Book.objects.get(book_id =book_id)
    return render(request, 'books/the_book.html',{"book":the_book})


#اضافه کردن کتاب جدید
def add_book_view(request):
    if request.method == "POST":

        form = request.POST
        form_images = request.FILES
        new_book = Book(
            Book_title=form['Book_title'],
            Book_category=form["Book_category"],
            book_image = form_images["book_image"],
            Book_auther= form['Book_auther'],
            book_slug = form['book_title'+'Book_auther'].replace(" ","-"),
            Book_price = form["Book_price"]
        )
        new_book.save()

        return HttpResponseRedirect(reverse("home"))
    else:
        print(f"====={request}=====")
    return render(request,'books/new_book.html')


def delete_view(request, book_slug=""):
    if book_slug != "":
        the_book = Book.objects.get(book_slug=book_slug)
        the_book.delete()
        return HttpResponseRedirect(reverse("delete"))
    all_books = Book.objects.all()
    return render(request, "books/delete.html", {"books":all_books})


def search_in_titles(request):
    if request.method == "GET":
        # get data
        data = request.GET
        # checks for empty search
        if data["search"] != "":
         
            # find search item in book titles
            search_results = Book.objects.filter(caption__contains=data["search"])
            return render(request,"books/search_result.html",{"results":search_results})
        else:
            return render(request,"books/404.html")
    else:
        return HttpResponse("not get")