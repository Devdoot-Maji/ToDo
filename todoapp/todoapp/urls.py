from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404, handler500

from todolist.views import addtask, index, deleteTask, doneTask, signup_view

urlpatterns = [
    path('developer/', admin.site.urls),
    path('index/', index, name="TodoList"),
    path('addtask/', addtask , name='addtask'),
    path('deletetask/<int:id>/', deleteTask , name='deletetask'),
    path('donetask/<int:id>/', doneTask , name='donetask'),
    path('signup/', signup_view , name="signup"),
    path("", auth_views.LoginView.as_view() , name="login"),
    path("logout", auth_views.LogoutView.as_view() , name="logout"),
]
