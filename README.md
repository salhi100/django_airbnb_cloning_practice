# Airbnb Cloning using Django

- My purpose is to make website for fitcuration: exercise recommendation system. 
- While taking Nomad Coders lectures, I don't recommend rewinding back.
  - [Instead, I recommend you to refer to the final result.](https://github.com/nomadcoders/airbnb-clone) 
  - First, Code with the instructor.
  - Second, Make your project 
  - Summary is important, but is least priority. When multitasking(phone call), summarize github log for your future self. 

## Django Project Folder & File Structure

- [config folder](./config) is master folder
- rest of folders are just applications. 
- applications are group of functionalities

### [Project configuration folder's](./config) structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- init.py helps to work like python package
- urls.py: controls url of the website. Can also be established under application. 

### Individual application folders' structure

- apps.py: configuration file which is installed [at the project's settings.py](./config/setttings.py)
- models.py: describing how database look like.
- admin.py: reflects changes on models.py to admin panel
- views.py: function that renders html
- urls.py: you can create urls.py under an application.
  like /users/profile, /users/delete, /users/register etc.

## [Notes: Initializing a Django Project](./_notes/1_Creating_a_Django_Project.md)

- Making Virtual Environment
- Installing django
- Selecting linter as flake8 and formatter as black
- SECURITY TIP: HOW TO KEEP SECRET_KEY SAFE

## [Notes: Building Applications and Models](./_notes/2_Building_Applications_and_Models.md)

- Building Users Applications inheriting Django's AbstractUsers class
- Building Core Application to reduce repetitive configuration in each applications.
- Building Rooms, Reviews, Reservations, Lists, Conversatiosn application
  1. register on settings.py
  2. shape database with models.py
  3. connect admin panel page with database at admin.py
  4. Make migrations and migrate

## [Notes: Making Admin Panel & Using Django Queryset](./_notes/3_Building_Admin_Panel.md)

```
<QuerySet [<User: myam>]>
```

- Querysets are list.
  - Objects are either manytomany, or foreignkey(=onetomany). 
  - In the example above, <User: myam> is foreignkey.
- Adding fields to admin panel
- "super" in Python

## [Notes: Seeding Data to Database, not through Admin Panel](./_notes/4_Seeding_Data_(NOT_by_Admin)_&_Fake_Data.md)

- Seedng fake data using faker
- Seeding list files to database

## [Notes: Views and URLs](./_notes/5_Views_and_URLs.md)

- Use Django Template for formatting HTML file that Django can render
- urls.py is request
- views.py is response









# 14 User Log in & Log out



# 15 Sign Up 





# 16 Verify Email



# 17 Log in with Github







# 18 Kakao Log in





# 19 Intro to Tailwind CSS







# 20 Design





# 21 User Profile, Edit Profile, Change Password







# 22 Room Detail





# 23 Update Room, Create Room, Room photos



# 24 Reservations and Reviews





# 25 Translations, lists and messages





# 26 Deployment to AWS





### My development environment

- System: Mac OS(10.15.3, Cattalina) 
- Python: 3.8.1 64bit
- Module information is stated in requirements.txt

## 





