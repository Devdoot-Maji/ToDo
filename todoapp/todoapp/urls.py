from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from todolist.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name="TodoList"),
]
