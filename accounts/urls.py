from django.urls import path
from .views import login_view,signup_view,main_page_view

urlpatterns = [
    path("", main_page_view, name='main_page'),
    path("login/",login_view,name='login'),
    path("signup/",signup_view,name='signup'),
    
    ]