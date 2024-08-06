Aqui está um guia passo a passo para criar um mini projeto em Django, adequado para uma introdução com estudantes que estão começando a aprender a framework. Este projeto será uma aplicação simples de lista de tarefas (To-Do List).

### Passo 1: Configuração do Ambiente
1. **Instalar Python**: Certifique-se de que Python está instalado. Recomendo a versão 3.8 ou superior.
2. **Criar um Ambiente Virtual**:
   ```bash
   python -m venv venv
   ```
3. **Ativar o Ambiente Virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Instalação do Django
1. **Instalar Django**:
   ```bash
   pip install django
   ```

### Passo 3: Criar o Projeto Django
1. **Criar um Novo Projeto**:
   ```bash
   django-admin startproject todoproject
   ```
2. **Entrar na Pasta do Projeto**:
   ```bash
   cd todoproject
   ```

### Passo 4: Criar a Aplicação Django
1. **Criar uma Aplicação**:
   ```bash
   python manage.py startapp todo
   ```
2. **Adicionar a Aplicação no `settings.py`**:
   - Abra `todoproject/settings.py` e adicione `'todo'` na lista `INSTALLED_APPS`.

### Passo 5: Definir o Modelo
1. **Criar o Modelo para Tarefas**:
   - Abra `todo/models.py` e adicione:
     ```python
     from django.db import models

     class Task(models.Model):
         title = models.CharField(max_length=100)
         completed = models.BooleanField(default=False)

         def __str__(self):
             return self.title
     ```
2. **Criar e Aplicar Migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Passo 6: Criar a View e Template
1. **Criar uma View para Listar Tarefas**:
   - Abra `todo/views.py` e adicione:
     ```python
     from django.shortcuts import render
     from .models import Task

     def task_list(request):
         tasks = Task.objects.all()
         return render(request, 'todo/task_list.html', {'tasks': tasks})
     ```
2. **Criar o Template**:
   - Crie uma pasta `templates` dentro da pasta `todo` e dentro dela uma pasta `todo`.
   - Crie um arquivo `task_list.html` dentro de `todo/templates/todo/` com o seguinte conteúdo:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>To-Do List</title>
     </head>
     <body>
         <h1>To-Do List</h1>
         <ul>
             {% for task in tasks %}
                 <li>
                     {{ task.title }} - {% if task.completed %}Completed{% else %}Pending{% endif %}
                 </li>
             {% endfor %}
         </ul>
     </body>
     </html>
     ```

### Passo 7: Configurar URLs
1. **Configurar URLs da Aplicação**:
   - Crie um arquivo `urls.py` dentro da pasta `todo` e adicione:
     ```python
     from django.urls import path
     from . import views

     urlpatterns = [
         path('', views.task_list, name='task_list'),
     ]
     ```
2. **Incluir URLs da Aplicação no Projeto**:
   - Abra `todoproject/urls.py` e modifique para:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('todo.urls')),
     ]
     ```

### Passo 8: Rodar o Servidor
1. **Rodar o Servidor de Desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

2. **Acessar a Aplicação**:
   - Abra o navegador e vá para `http://127.0.0.1:8000/`.

### Passo 9: Populando o Banco de Dados
1. **Acessar o Admin do Django**:
   - Crie um superusuário para acessar o admin:
     ```bash
     python manage.py createsuperuser
     ```
   - Siga as instruções para criar o superusuário.
2. **Adicionar Tarefas via Admin**:
   - Acesse `http://127.0.0.1:8000/admin/`, faça login com o superusuário criado.
   - Adicione algumas tarefas para que possam ser visualizadas na aplicação.

### Conclusão
Com esses passos, você e seus estudantes terão uma aplicação básica de To-Do List funcionando. Este guia cobre os fundamentos do Django e proporciona uma experiência prática, sem entrar em conceitos muito profundos. Boa aula!