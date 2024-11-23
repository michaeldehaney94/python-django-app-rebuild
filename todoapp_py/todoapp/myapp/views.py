from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Task


# Create your views here.


# Get list of data and add data
def index(request):
    task_list = Task.objects.all()

    # request to add new task on the same webpage
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')  # redirect to homepage

    return render(request, 'myapp/index.html', {'task_list': task_list})


# delete task
def delete(request, taskid):
    task = Task.objects.get(id=taskid)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'myapp/edit.html', {'form': form, 'task': task})
