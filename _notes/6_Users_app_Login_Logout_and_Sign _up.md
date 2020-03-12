# 6. Users app: Login, Logout and Sign up



- **template: user interaction**
  - [sends {{form}} to forms.py](./templates/users/login.html)
  - [routes {% url "users:signup" %} to urls.py](./templates/partials/nav.html)
- **urls.py: connection between views.py and template**
  - urlpatterns
    - utilizes classes & functions from user app's views.py 
    - export views.py classes & functions to templates as name="name"
  - app_name: exports user's url routing to django project
- **views.py: controller which provides functions and methods from django classes** 
  - Classes & methods : FormView ...
  - Functions: render, redirect, reverse, authenticate, logout...
  - receives functions and methods from forms.py
  - **Through urls.py, supplies functions and methods to templates **
- **forms.py: branched off from views.py, receives forms from template and processes certain actions**
  - need to manually create a file in users app folder
  - **process get requests from template**
  - get queryset objects from models.py, validates password and username(=email)
  - **sends class and methods back to views.py**

### MVC Architecture in Django

From YouTube Cloning class:

- Model: Model represents shape of the data.
- View: View is a user interface.
- Controller: Controller handles the user request.

For Django project, if I were to match MVC architecture to individual python files:

- Model <-> models.py
- View <-> templates (.html & .css)
- Controller <-> views.py, forms.py

https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f

![picture](https://miro.medium.com/max/1276/1*pHlF3KufWwX7svv4Mv4Frg.jpeg)

# 14 User Log in & Log out

- FormView to replace Django's default class LoginView
- 

# 15 Sign Up 





# 16 Verify Email



# 17 Log in with Github







# 18 Kakao Log in



