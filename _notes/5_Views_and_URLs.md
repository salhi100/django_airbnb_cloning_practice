# 10. Views and URLs

- Use Django Template for formatting HTML file that Django can render

- urls: request 

  - ex) Log-in, password from users

- views: response 

  - ex) rendered HTML

- {{}}: inserting Python logics in static template

- Inheritance for html

  - base.html is base structure (or father class) of static html files
  - Just like extending in pug

- Block is window that we can fill children templates contents in father's templates.

  - create blocks in base.html 
  - use blocks in all_rooms.html
  - create partials such as footers, headers and include it on base.html

- [At ./config/settings.py ](./config/settings.py ), change the following

  ```python
  "DIRS": [os.path.join(BASE_DIR, "templates")],  # where to look for templates
  ```

- [./config/urls.py](./config/urls.py) 

  - serves as routes.js

- [./core/urls.py](./core/urls.py) 

  - serves as globalRouter.js
  - [urls.py](./core/urls.py) needs to be made manually in core apps folder

- [./rooms/urls.py](./rooms/urls.py)

  - serves as roomRouter.js

- [./rooms/views.py](./rooms/views.py) 

  - serves as controller.js.
  - views.py is between ./app/models.py and html static files using context
  - controlls html file with context

# 11. HomeView

Before learning Django class based views, we should know what's going on behind pagination. 

### 1. Hard Coding Pagination

- [using views.py and html file to manually make page 1 ~ 15 navigation on lower bar](https://github.com/snoop2head/django_airbnb_cloning/commit/1af8a6e64bb8f19f4d765ebd514b71050117455b)
- [pagenation manually done: simple logic using django built-in template tags on static html file](https://github.com/snoop2head/django_airbnb_cloning/commit/dc35af21ba30416d98b6bb3273897bdfa03b7d4c)

### 2. Semi Coding Pagination

- [using django paginator class and methods](https://github.com/snoop2head/django_airbnb_cloning/commit/6e93b5d56cfe691d3ba3d623585c6e503ae43b5f)
- [using methods in paginator class to paginate website](https://github.com/snoop2head/django_airbnb_cloning/commit/bf1facb38f0b64bc2bab48db7e62eae3160e042f)
- [django handling exceptions, redirecting to home when page number exceeds](https://github.com/snoop2head/django_airbnb_cloning/commit/0e80d145bab4a40084d8f2c1b159f957324c5a98)

### 3. Using Class Based Views

- [Simplest: inheriting ListView class to paginate](https://github.com/snoop2head/django_airbnb_cloning/commit/ef5c4d017928b1a0a5133b94504893d790f5e006)

# 12 DetailView

- ./rooms/detail.html: static template
- ./rooms/views.py: responds by returning rendered template to users request 
- ./config/urls.py: routing to "http://127.0.0.1:8000/rooms/"
- ./rooms/urls.py: routing views file to path "http://127.0.0.1:8000/rooms/1"

Designating namespace as such:

"rooms:detail" room.pk 
<=> 
"namespace:path" object.arguments

```html
<a href="{/rooms/{{room.pk}}}"> {{room.name}} / ${{room.price}} </a>
```

can be simply be written as

```python
# ./config/urls.py
path("rooms/", include("rooms.urls", namespace="rooms")),

# ./rooms/urls.py
urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
```

```html
<!-- room_list html static template -->
<a href="{% url "rooms:detail" room.pk %}"> {{room.name}} / ${{room.price}} </a>
```



Similarly, 

```html
<a href="/">AirBnB</a>
```

can be rewritten as

```html
<a href="{% url "core:home" %}"> AirBnB</a>
```



# 13 SearchView

### Development Workflow: Function Based Views

- [Make form on template at html](./templates/rooms/search.html)
- Receive from template as get request at views.py. [Inside views.py, there are three parts:](./rooms/views.py)
  - Get request: form which receives user request
  - Querying database: refer to fields names at models.py and get objects.
  - Reponse: render html file or raise error
- Go back to template at html and write out response based on context in views.py
- Using context, we reflect user request and queryset choices to search.html.
- slugify is turning amenity.pk (int) into string
- checked in html is remembering checkbox as checked
- "Remembering Option" is not remembering option on html. To make such function, 

  1. Make template that receives user request. Types are: input(text search input), option(dropdown), checkbox, number(number input) etc..
  2. On views.py, receive user's get request as form, renders back to template as context.
  3. Responds with html template with context variable displayed on html. Wrap with bracket as such {{context_variable}}, or {if context_variable}
- [Refer to Field Lookups for querying, filtering data](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#field-lookups)
- Boolean is True, False. change "on" to True with bool()

### Making Forms: Class Based Views

- Form makes HTML template for you referencing models.py database fields
