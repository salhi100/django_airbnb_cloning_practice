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

  - serves as globalrouter.js
  - [urls.py](./core/urls.py) needs to be made manually in core apps folder

- [./rooms/views.py](./rooms/views.py) 

  - serves as controller.js.
  - views.py is between ./app/models.py and html static files using context
  - controlls html file with context

# 11. HomeView

## We Learn Three Methods 

### Hard Coding



### Semi Coding



### Using Class Based Views



- Calling Django function from static template 
- Abastracting paginator is possible

# 12 DetailView





# 13 SearchView