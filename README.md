# Airbnb Cloning using Django

- My purpose is to make website for fitcuration: exercise recommendation system. Thus, I am cloning Airbnb as tutorial with Django & Tailwind.
- **While taking lectures, I don't recommend rewinding back.**
  - [Instead, I recommend you to refer to the final result.](https://github.com/nomadcoders/airbnb-clone) 
  - First, Code with the instructor.
  - Second, Make your project 
  - Summary is important, but is least priority. When multitasking(phone call), look at github log and explain your code to yourself. 
- My development environment is the following:
  - System: Mac OS(10.15.3, Cattalina) 
  - Python: 3.8.1 64bit
  - Module information is stated in requirements.txt

## Django Project Folder & File Structure

- [config folder](./config) is master folder
- rest of folders are just applications. applications are group of functionalities

### [Project configuration folder's](./config) structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- init.py helps to work like python package
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



# [Initializing a Django Project](./_notes/1_Creating_a_Django_Project)



# [Building Applications and Models](./_notes/2_Building_Applications_and_Models)

### 

# [Making Admin Panel & Using Django Queryset](./_notes/3_Building_Admin_Panel)



# [Seeding Data to Database, not through Admin Panel](./_notes/4_Seeding_Data_(NOT_by_Admin)_&_Fake_Data)



# [Views and URLs](./_users/5_Views_and_URLs)







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











