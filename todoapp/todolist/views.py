from django.shortcuts import render
from django.shortcuts import redirect
from .models import TodoList
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse("TodoList"))
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def index(request):
    todos = TodoList.objects.filter(user=request.user)
    return render(request,'index.html',{"todos": todos})

@login_required
def addtask(request):
    todos = TodoList.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            content = request.POST["content"]
            date = str(request.POST["date"])
            user = User.objects.get(id=request.user.id)
            Todo = TodoList(title=title, content=content, date=date, user=user)
            Todo.save()
            return redirect(reverse("TodoList"))
    return render(request, "addtask.html", {"todos": todos})

def deleteTask(request,id):
    todos = TodoList.objects.get(id=id)
    todos.delete()
    return redirect(reverse("TodoList"))

def doneTask(request,id):
    todo = TodoList.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect(reverse("TodoList"))
