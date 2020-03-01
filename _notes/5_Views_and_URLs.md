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

Before learning Django class based views, we should know what's going on behind classes. 



### 1. Hard Coding

- github log

### 2. Semi Coding

- github log

### 3. Using Class Based Views

- github log

- Calling Django function from static template 
- Abastracting paginator is possible
- 

# 12 DetailView

- ./rooms/detail.html: static template
- ./rooms/views.py: responds by returning rendered template to users request 
- ./config/urls.py: routing to "http://127.0.0.1:8000/rooms/"
- ./rooms/urls.py: routing views file to path "http://127.0.0.1:8000/rooms/1"

Designating namespace to simplify routing

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
{% comment %} room_list html static template {% endcomment %}
<a href="{% url "rooms:detail" room.pk %}"> {{room.name}} / ${{room.price}} </a>
```

"rooms:detail" room.pk
"namespace:path" object.arguments



Similarly, 

```html
<a href="/">AirBnB</a>
```

can be rewritten as

```html
<a href="{% url "core:home" %}"> AirBnB</a>
```



# 13 SearchView

