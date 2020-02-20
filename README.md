# Airbnb Cloning using Django

- My purpose is to make website for fitcuration: exercise recommendation system. Thus, I am cloning Airbnb as tutorial with Django & Tailwind.
- **While taking lectures, I don't recommend rewinding back.**
  - [Instead, I recommend you to refer to the final result.](https://github.com/nomadcoders/airbnb-clone) 
- My development environment is the following:
  - System: Mac OS(10.15.3, Cattalina) 
  - Python: 3.8.1 64bit
  - Module information is stated in requirements.txt

# 1. Django Project Folder & File Structure

- [config folder](./config) is master folder
- rest of folders are just applications. applications are group of functionalities

### [Project configuration folder's](./config) structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- __init__.py helps to work like python package
- urls.py: controls url of the website. Can also be established under application. 

### Individual application folders' structure

- apps.py: configuration file which is installed [at the project's settings.py](./config/setttings.py)
- admin.py: reflects changes on admin panel
- models.py: describing how database look like.
  - Models have fields.
  - For the fields you put in models.py, will make be turned into database table. 
  - Django ORM translates python code into SQL Instructions to database.
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

- **MAKE SURE YOU ARE INSIDE THE BUBBLE.** 

- Then, setup configuration for the django. 

```shell
pip install django
django-admin startproject config
```
- Drag config directory and manage.py file out of the original config directory. Manually change the config directory of the project (NOT USING CONSOLE)

- You can change python settings on the low deck of VSCode. 

- Go to manage.py Python file. VSCode will tell you to setup linter and formatter.

  - Recommending flake 8 as linter. it is automatically recommended through vscode 

  - Recommending black as formatter. 

    - If formatter isn't recommended bia VSCode, then commence the following:

      ```shell
       pip install black --dev --pre
      ```

  - Selecting linter and formatter for the project is recorded on .vscode/settings.json file

### manage.py: database and server

- **[Refer to manage.py related Django documents here](https://docs.djangoproject.com/en/3.0/ref/django-admin/)**

- Run your server, Where pipenv is activated (= inside the bubble).

```shell
python manage.py runserver
```

Or, if you want to run on different port, 

``` shell
python manage.py runserver 7000
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

- [Make .gitignore file referencing this link](https://github.com/github/gitignore/blob/master/Python.gitignore)
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

[What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

- Django project is group of applications (= just say Django is a group of functions).
- When to create application / when not to create application is important. 
- We should not have so much functionality in one folder(=application)
- **You should be able to describe an application in one sentence.** If you use the word "and", then it should be diferent application. **Divide and conquer**
- For example, listing application will be consisted with functions as such: Create list, Read List, Update List and delete list 

# 3. Building Users Applications: /users directory

### Creating Apps

```shell
 django-admin startapp [appname]
```

- since app contains multiple functions, appname should be in plural form
- names of .py files in application folder is not optional. You can't change names
- for example, users app has create password, update password

### How to make Users Application

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

- **[Refer to models.py fields document on Django](https://docs.djangoproject.com/en/2.2/ref/models/fields/).** 
- textfield: yields text field without limit on webpage
- charfield: yields text field with limit of single line webpage
- datefield: yields calendar selection on webpage
- boolean field: true of false checkbox

![image-20200214211005945](/Users/noopy/Library/Application Support/typora-user-images/image-20200214211005945.png)

### admin.py: Admin Panel 

- **[Refer to admin.py fields document document on Django](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)**
- admin.py regards about admin panel of the website. 
- you can create filter(like excel) for fields in table: such as currency or superhost



# [4. Building Rooms Applications](./rooms)

## [Refer to cloning webpage. Rooms App's functions are: ](*https://www.airbnb.com/rooms/22320269?location=Seoul&source_impression_id=p3_1581697502_PpMPhvPC73I2KD%2BU*)

- room register
- room photo upload
- describing room's specifications(price, option, type...)

## [Making Core Application](./core)

- This is application that is not visible to users. 

  - The purpose of this app is to simplify repetetive calling onto certain model: such as timestamp
    - [In this app's models.py, we made TimeStamped class](./core/models.py) as subject for the call up
    - [TimeStamped class](./core/models.py) will be used in all the other apps.
    - [On the other hand, Users app imported AbstractUser class from Django default models only](./users/models.py).

- All the other application names should be plural, except for this kind of application.

- In other apps' models.py, you can import Core Application's models along with default django models

  ```python
  #importing django default models as class
  from django.db import models 
  
  #importing Core Application's models as class
  from core import models as core_models #"as" is like "import pandas as pd"
  ```

## WorkFlow when creating Rooms app

### 1. [At project's settings.py](./settings.py), install apps that I built. This is to let Django project know which are apps.py to use for the project.

``` python
# Letting Django know my established Project apps by stating here.
# Importing apps.py in each apps: core, users, rooms, reviews ...
PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
]

# Put users auth at the end
AUTH_USER_MODEL = "users.User"
```



### 2. [At individual application's models.py,](./rooms/models.py) shape database & connect between tables of other application's models.py

- **Write packages / modules in order**

``` py
# first django
from django.db import models

# second third party apps
from django_countries.fields import CountryField

# third my applications
from core import models as core_models
```

- **[Foreign Key (one to multiple) in models.py](https://docs.djangoproject.com/en/3.0/ref/models/fields/)**
  - foreign key is connecting one model to the many other. source of the connection is user, and it connects to multiple rooms.
  - Room database(or table) looks like this ![image-20200215131251118](/Users/noopy/Library/Application Support/typora-user-images/image-20200215131251118.png)
  - Foreign Key(FK:USER) calls data from another database(or sheet), which is user table.
    ![image-20200215131329179](/Users/noopy/Library/Application Support/typora-user-images/image-20200215131329179.png)

  - For example, many instagram posts per user or many youtube posts per google user.

- **[Many to Many Relationship in models.py](https://docs.djangoproject.com/en/3.0/ref/models/fields/)**
  - models.ManyToManyField(<>)
- All of other classes above are inherited in Room class

``` python
# Shaping Database(or table) of rooms
# All of classes above are inherited here.
class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    # when requiring fill up, don't put blank=True
    # Below are different types of fields that we can utilize

    #Charfield and textfield
    name = models.CharField(max_length=140)
    city = models.CharField(max_length=80)
    description = models.TextField()
    
    #country field is inhereted from third party
    country = CountryField()

    
    #integerfield example
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
		
    #timefield example
    check_in = models.TimeField()
    check_out = models.TimeField()
    
    #booleanfield(checkbox) example
    instant_book = models.BooleanField(default=False)
    
    # foreignkey field
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    

```

### 3. [At individual application's admin.py](./rooms/admin.py), register table models that you built previously.  

``` python
from django.contrib import admin
from . import models  # from the same folder, import the application's models

# refer to ./models.py for which models to register
# registering multiple models at once
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass
```



### 4. Since we shaped tables in models.py & reflected change of database on admin panel, makemigrations and migrate

```shell
python manage.py makemigrations
python manage.py migrate
```

### 5. At the webpage, check Admin panel.

![image-20200216003543786](/Users/noopy/Library/Application Support/typora-user-images/image-20200216003543786.png)

### 6. [At individual application's models.py,](./rooms/models.py) setup verbose name to forcefully designate names that is displayed on Admin webpage.

![image-20200216004144914](/Users/noopy/Library/Application Support/typora-user-images/image-20200216004144914.png)

# [5. Other Applications](./reservations)

### - Reviews application

### - Reservations application

### - Lists application

### - Conversations application



# [6. Room Admin Panel & Site](./rooms/admin.py)

- Making representative tables on webpage
- Making Search fileds
- Creating Filter



# [7 Django Queryset](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#django.db.models.query.QuerySet)

- ```shell
  <QuerySet [<User: myam>]>
  ```

  1) Querysets are list.

  2) Objects are either manytomany, or foreignkey(=onetomany). In the example above,  <User: myam> is foreignkey.

## How to look up querysets

- Run manage.py shell
  
  ```shell
  pipenv shell
  python manage.py shell
  ```
  
- vars to look up simple information, dir to look up specific information in database

  ```python
  from users.models import User
  vars(User)
  dir(User)
  ```

### Getting foreignkeys & manytomany Queryset

- [In this case, reviews is poining at users(=myam) with foreignkey.](./reviews/models.py)

  ```python
  user = models.ForeignKey(
          "users.User", related_name="reviews", on_delete=models.CASCADE
      )
  ```

  Thus, we can get querysets for reviews. 

  ```python
  myam = User.objects.get(username="myam")
  vars(myam)
  dir(myam)
  myam.reviews.all()
  ```

- [In this case, reviews is pointing at rooms with foreignkey](.reviews/models.py) 

  ```python
  # pointing rooms tables with reviews database
  room = models.ForeignKey(
    "rooms.Room", related_name="reviews", on_delete=models.CASCADE
  )
  ```

  Thus, we can get querysets for reviews and amenities

  ```python
  from rooms.models import Room
  room = Room.objects.get(id=1)
  room
  room.reviews.all()
  ```

- [In this case, many to many relationship is established between amenities and rooms.](./rooms/models.py)

  ```python
  amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
  ```

  Thus, we can get querysets for amenities.

  ```python
  room.amenities.all()
  ```

  Or, we can get queryset with the following method also. 

  ```python
  from rooms.models import Amenity
  Amenity.objects.all()
  a = Amenity.objects.get(id=1)
  a.rooms.all() 
  ```

- In order to get queryset, instead of this,

  ```shell
   room.review_set -> WRONG
  ```

  Do this to get queryset (from reviews).

  ```python
  room.reviews.all()
  ```

- **You should use related_names field in models.py in order to get queryset.**
  
- **related_names is for the target.** [Next example is when rooms/models.py points users table with foreignkey](./rooms/models.py), but didn't set related_name inside of field.
```python
  host = models.ForeignKey(
          "users.User", on_delete=models.CASCADE
      )
```

In this case. At Manage.py Shell, when you look up  queryset of users received from rooms, You'll have following error.

```python
  myam.rooms.all()
  ------------------------------------
  "AttributeError: 'myam' object has no attribute 'rooms'"
```

따라서 [rooms의 models.py에서](./rooms/models.py) users로 pointing한다. users과 rooms을 연결하는 foreignkey 부분에 related_name을 추가함으로서, users에 "rooms"라는 queryset을 보낸다.

  ```python
  host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
      )
  ```

  [이에 대한 관련 내용은 Foreignkey에서 related_name으로 query를 짜는 법 문서를 참조하라.](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

Filtering queryset: get queryset with specified options

- filtering

  ```python
  from users.models import User
  all_user = User.objects.all()
  all_user.filter(superhost=True)
  ```

- ```python
  startswith = User.objects.filter(username__startswith="noo")
  print(startswith)
  ```

  if you run this, you will get noopy. 



