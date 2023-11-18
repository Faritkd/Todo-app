from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.

def todo_list(request: HttpRequest):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    form = TodoForm()
    context = {
        'form': form,
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def remove(request: HttpRequest, id: int):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('todo_list')


