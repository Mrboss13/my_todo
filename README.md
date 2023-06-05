# Todo-api project

this is simple CRUD based api project with user authentication 

## steps for install project
step1:  run virtual environment by running following command
```bash
  todo_env/Scripts/activate
```
step2: install dependancies by run following command
```bash
  pip install -r requirements.txt
```
step3: run following command for database sqlquery
```bash
  python manage.py makemigrations
```
step4: after makemigrations run following command for create database
```bash
  python manage.py migrate
```
step5: till now if the all command work with no error then now create a superuser for interact with admin panal and authenticate in api run the following command
```bash
  python manage.py createsuperuser
```
after run type the  detail

step6: after run all command now start django develovement server by run following command
```bash
  python manage.py runserver
```



