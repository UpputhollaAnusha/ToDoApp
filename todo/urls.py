from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from . import views 
from django.urls import path 
urlpatterns=[

    path('normal',views.normalView,name="normal"),
    path('todolist',views.todoappView,name="todolist"),
    path('ItemAdd',views.ItemAddView,name='Add'),
    path('delete/<int:i>',views.deleteTodoView),
    #path('login',LoginView.as_view(),name="login"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]