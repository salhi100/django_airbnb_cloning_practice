# Airbnb Cloning using Django

- My purpose is to make website for fitcuration: exercise recommendation system. 
- Thus, I am cloning Airbnb as tutorial with Django & Tailwind.
- **While taking lectures, I don't recommend rewinding back.**
- [**Instead of rewinding, refer to the final result. You can prevent yourself being stuck on making one specific part**](https://github.com/nomadcoders/airbnb-clone) 
- My development environment is the following:
  - System: Mac OS(10.15.3, Cattalina) 
  - Python: 3.8.1 64bit
  - Module information is stated in requirements.txt

# 1. Folder & File Structure

- config folder is master folder
- rest of folders are just applications. applications are group of functionalities

### configuration folder structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- __init__.py helps to work like python package
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

- MAKE SURE YOU ARE INSIDE THE BUBBLE. Then, setup configuration for the django. 

```shell
pipenv install django
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

- [Make .gitignore file referencing this link](https://github.com/github/gitignore/blob/master/Python.gitignore)

### manage.py: database and server

- Run your server, Where pipenv is activated (= inside the bubble).

```shell
python manage.py runserver
```

- You'll have localhost connection.
- You can also access to admin panel page, which is  http://127.0.0.1:8000/admin/login/?next=/admin/
- Without manage.py, database table doesn't exist. Thus this kind of error will appear on console log, if you run server for the second time.
**You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.**
- SQL needs to learn how database look like. 
- You change the shape of data(=creating migration), and migrate to update database
- Updating Database: Django shapes the data(or change the shape), you create migration, you apply migration
- Therefore, configurate SQL(Structured Queried Language) database with 

```shell
python manage.py migrate
```

### Security & Other Tips

- For those uploaded their django repository publicly, keep your SECRET_KEY in settings.py away from the others!
  - [English Instructiions on how to keep SECRET_KEY safe](https://www.quora.com/Is-it-possible-to-change-the-secret-key-of-a-Django-application-after-it-deployment-in-production-If-so-what-would-be-the-impacts)
  - [SECRET_KEY를 안전하게 보관하는 법 국문 가이드](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)
- Even if you successfully removed SECRET_KEY from settings.py, git history of the file is still accessible in github on public. So it is still dangerous to keep(or to publish) your repo as public repo.
  - [WARNING: all of your GIT history will be cleared after commencing the next process] 
    [Follow the steps of this link in order to clear up git history, and commit as initial commit.](https://gist.github.com/stephenhardy/5470814) 
  - If files & file contents were to be pages in a book, Git history is like bookmarks. Clearing git history will not affect current files/directories on your project. 
  - However, removing git history means your previous versions(NOT current versions) are inaccessible. For example, you can’t revert your project files to version you worked on a week ago. 
- [In Django documentation, you can even look up the code.](https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/password_validation/#CommonPasswordValidator)
- On VSCode Windows, CMD + Mouse Click on function to see the source code 

### Projects vs. apps

- Django project is group of applications (= just say Django is a group of functions).

[What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

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



# 3. Building Users Applications: /users directory

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

### **[Refer to fields document on Django](https://docs.djangoproject.com/en/2.2/ref/models/fields/).** 

- textfield: yields text field without limit on webpage
- charfield: yields text field with limit of single line webpage
- datefield: yields calendar selection on webpage
- boolean field: true of false checkbox

![image-20200214211005945](/Users/noopy/Library/Application Support/typora-user-images/image-20200214211005945.png)

### Admin.py: Admin Panel 

### **[Refer to admin fields document document on Django](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)**

- admin.py regards about admin panel of the website. 
- you can create filter(like excel) for fields in table: such as currency or superhost



# 4. Building Rooms Applications: /rooms directory

### [App's funcitions are: room register, room photo upload and describe room(price, option, type...)](*https://www.airbnb.com/rooms/22320269?location=Seoul&source_impression_id=p3_1581697502_PpMPhvPC73I2KD%2BU*)

- Write packages / modules in order

``` py
# first django
from django.db import models

# second third party apps
from django_countries.fields import CountryField

# third my applications
from core import models as core_models
```

### [Foreign Key (one to multiple)](https://docs.djangoproject.com/en/3.0/ref/models/fields/)

- foreign key is connecting one model to the many other. source of the connection is user, and it connects to multiple rooms.

- Room database(or table) looks like this 

  ![image-20200215131251118](/Users/noopy/Library/Application Support/typora-user-images/image-20200215131251118.png)

- Foreign Key(FK:USER) calls data from another database(or sheet), which is user table.
  ![image-20200215131329179](/Users/noopy/Library/Application Support/typora-user-images/image-20200215131329179.png)

- For example, many instagram posts per user or many youtube posts per google user.

### Many to Many Relationship

- 

- 

### Other Characteristics

- All of classes above are inherited in Room(core_models.TimeStampedModel)
- TimeStamped model is to skip repeating calling Django model. 
  - This will be used in all the other apps, except for Users app.

## WorkFlow when creating app

1. shaping database & connecting between tables at models.py
   ![image-20200216003744519](/Users/noopy/Library/Application Support/typora-user-images/image-20200216003744519.png)

2. registering models at admin.py

   ![image-20200216003655368](/Users/noopy/Library/Application Support/typora-user-images/image-20200216003655368.png)

3. Check Admin panel of the webpage

![image-20200216003543786](/Users/noopy/Library/Application Support/typora-user-images/image-20200216003543786.png)

4. Setup Verbose name to fix the mess on Admin webpage

![image-20200216004144914](/Users/noopy/Library/Application Support/typora-user-images/image-20200216004144914.png)

