**Adım 1: Django Projesi Oluşturma**

Öncelikle Python'ı bilgisayarınıza yükleyin (https://www.python.org/downloads/).
Terminali açın ve aşağıdaki komutu kullanarak Django framework'ünü yükleyin:

pip install Django

Ardından, bir Django projesi oluşturmak için aşağıdaki komutu kullanın:

django-admin startproject todo_list

Proje oluşturulduktan sonra, projenin dizinine giriş yapın:

cd todo_list

**Adım 2: Uygulama Oluşturma**

Bir uygulama oluşturmak için aşağıdaki komutu kullanın:

python manage.py startapp todo

Oluşturulan uygulamayı projeye dahil etmek için settings.py dosyasını açın ve INSTALLED_APPS bölümüne 'todo' satırını ekleyin.

**Adım 3: Model Oluşturma**

todo dizininde models.py dosyasını açın ve aşağıdaki gibi bir model tanımlayın:

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


Modeli oluşturmak için aşağıdaki komutu kullanın:

python manage.py makemigrations
python manage.py migrate

**Adım 4: URL Yönlendirme**

todo dizininde urls.py dosyasını oluşturun ve aşağıdaki kodu ekleyin:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]


Projenin ana urls.py dosyasını açın ve urlpatterns listesine todo/ yolunu ekleyin.

**Adım 5: Görünümler (Views) Oluşturma**

todo dizininde views.py dosyasını açın ve aşağıdaki kodu ekleyin:

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'form': form})

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/update_task.html', {'form': form, 'task': task})

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

forms.py dosyasını oluşturun ve aşağıdaki kodu ekleyin:

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)


**Adım 6: Şablonlar (Templates) Oluşturma**

templates dizini oluşturun ve içine todo adında bir klasör oluşturun.
task_list.html adında bir dosya oluşturun ve aşağıdaki kodu ekleyin:

{% for task in tasks %}
    <div>
        <h3>{{ task.title }}</h3>
        <p>Completed: {{ task.completed }}</p>
        <p>Created At: {{ task.created_at }}</p>
        <a href="{% url 'update_task' task.pk %}">Edit</a>
        <a href="{% url 'delete_task' task.pk %}">Delete</a>
    </div>
{% empty %}
    <p>No tasks available.</p>
{% endfor %}

<a href="{% url 'create_task' %}">Create Task</a>


create_task.html adında bir dosya oluşturun ve aşağıdaki kodu ekleyin:

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>

update_task.html adında bir dosya oluşturun ve aşağıdaki kodu ekleyin:

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>

**Adım 7: Sunucuyu Çalıştırma**

Terminalde, projenin ana dizininde aşağıdaki komutu çalıştırın:

python manage.py runserver

Tarayıcınızı açın ve http://localhost:8000/ adresine gidin. To-Do List uygulamasını görmelisiniz.





