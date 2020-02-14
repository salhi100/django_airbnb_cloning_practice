# Airbnb Clone

- Cloning Airbnb tutorial with Django, Tailwind
  - System: Mac OS(10.15.3, Cattalina) 
  - Python: 3.8.1 64bit
  - Module information is stated in requirements.txt
- Purpose is to make website for fitcuration: exercise recommendation system

# 1. Folder & File Structure

- config folder is master folder
- rest of folders are just applications. applications are group of functionalities

### configuration folder structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- __init__.py is helps to work like python package
- urls.py: controls url of the website. Can also be established under application. 

### application folder structure

- apps.py: just configuration file
- admin.py: reflects changes on admin panel
- models.py: describing how database look like.
  - Django ORM translates python code into SQL Instructions to database.
  - Whatever you put in models.py, Django will make it into database table. 
- views.py: function that renders html
- urls.py: you can create urls.py under an application.
  like /users/profile, /users/delete, /users/register etc.

# 2. Creating a Django Project

### How to Initiate Project

```shell
pipenv shell
```

- initiate virtual environment for project in the project's directory

- it will take some time for initial setup 

- In order to exit the virtual environment, deactivate 

  ```shel
  deactivate
  ```

  - or exit the virtual environment, If "UNKNOWN VIRTUAL ENVIRONMENT is already activated" error 

    ```shell
    exit
    ```

- setup configuration for the django

```shell
django-admin startproject config
```
- Drag config directory and manage.py file out of the original config directory. Manually change the config directory of the project (NOT USING CONSOLE)

- You can change python settings on the low deck of VSCode. 

- Go to manage.py Python file. VSCode will tell you to setup linter and formatter.

  - Recommending flake 8 as linter. it is automatically recommended through vscode 

  - Recommending black as formatter. 

    - If formatter isn't recommended bia VSCode, then commence the following:

      ```shell
       pipenv install black --dev --pre
      ```

  - Selecting linter and formatter for the project is recorded on .vscode/settings.json file

### manage.py: database and server

- Run your server, Where pipenv is activated (= inside the bubble).

```shell
python manage.py runserver
```

- You'll have localhost connection.
- You can also access to admin panel page, which is  http://127.0.0.1:8000/admin/login/?next=/admin/
- without manage.py, database table doesn't exist. Thus this kind of error appears on console log. 
**You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.**
- SQL needs to learn how database look like. 
- You change the shape of data(=creating migration), and migrate to update database
- Updating Database: Django shapes the data(or change the shape), you create migration, you apply migration
- Therefore, configurate SQL(Structured Queried Language) database with 

```shell
python manage.py migrate
```

### Other Tips

- In Django documentation you can even look at code, like https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/password_validation/#CommonPasswordValidator
- On VSCode Windows, CMD + Mouse Click on function to see the source code 

### Projects vs. apps

- Django project is group of applications (= just say Django is a group of functions).

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
Source: https://docs.djangoproject.com/en/3.0/intro/tutorial01/

- We should not have so much functionality in one folder(=application)
- If it is folder of list, it should be simple as such: Create list, Read List, Update List and delete list 
- Applications should be separate. 
- Django project is made of many small applications. when to create application / when not to create application is important

**You should be able to describe an application in one sentence.** If you use the word "and", then it should be diferent application. **Divide and conquer**

```shell
 django-admin startapp [appname]
```
- since app contains multiple functions, appname should be in plural form
- names of .py files in application folder is not optional. You can't change names
- for example, users app has create password, update password



## 3. Building Users Applications: /users directory

- replacing django user with my user
- Python is object programming language: class can be inherited!
- CMD + click to check Abstractuser class
- Django makes migration by itself, so we don't have to write sql

```shell
python manage.py makemigrations
python manage.py migrate
```

- Django has database fields for everything: email field, text field... Just call for fields. 

![image-20200213015216499](/Users/noopy/Library/Application Support/typora-user-images/image-20200213015216499.png)

- installing module on python virtual environment SHOULD NOT BE DONE WITH pip. 
  Use pipenv

  ``` shell
  pipenv install Pillow
  ```

### models.py: All the fields are translated into database stuff.

[Refer to fields document on Django](https://docs.djangoproject.com/en/2.2/ref/models/fields/). 

- textfield: yields text field without limit on webpage
- charfield: yields text field with limit of single line webpage
- datefield: yields calendar selection on webpage
- boolean field: true of false checkbox

![image-20200214211005945](/Users/noopy/Library/Application Support/typora-user-images/image-20200214211005945.png)

### Admin.py: Admin Panel 

[Refer to admin fields document document on Django](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)

- admin.py regards about admin panel of the website. 
- you can create filter(like excel) for fields in table: such as currency or superhost