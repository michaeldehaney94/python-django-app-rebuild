1. Create project folder and install django - pip install django <br/>
<br/>
2. Create django project - django-admin startproject [projectname]<br/>
<br/>
3. 'cd' into django project directory <br/><br/>
4. Create django app - django-admin startapp [appname]<br/><br/>
5. Create database models and table columns in models.py<br/><br/>
6. dd "myapp" to "INSTALLED_APPS" in settings.py<br/><br/>
7. Import and register database model to admin.py<br/><br/>
8. Run make migrations - py manage.py makemigrations<br/><br/>
9. Run migrations - py manage.py migrate<br/><br/>
10. Create superuser for django admin - py manage.py createsuperuser<br/><br/>
11. Run server - py manage.py runserver<br/><br/>
12. To create a model form to reduce recreating a form, create 'forms.py' in the myapp folder. Import 'from .models import Task' <br/>and 'from django import forms' in forms.py. Then create a view in view.py for updating data.

To run Django in localhost, open terminal and run "py manage.py runserver"
