from django.shortcuts import render
from .models import TodoList

def index(request):
    todos = TodoList.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, date=date)
            Todo.save()
            return redirect("/")
    return render(request, "index.html", {"todos": todos})