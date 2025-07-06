from django.urls import path
from books.views import *


urlpatterns = [
    path("",home_view, name='home'),
    path("<slug:slug>", book_detail, name="book"),
    # path('book/<slug:slug>/', views.book_detail, name='book_detail'),
    path("add/", add_book_view, name='add_book'),
    path("search/",search_in_titles, name="search_url"),
    path("remove/",delete_view,name="delete")
]