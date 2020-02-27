Pull request for seed_lists.py



Traceback (most recent call last):
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: UNIQUE constraint failed: lists_list.user_id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py", line 328, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/core/management/base.py", line 369, in execute
    output = self.handle(*args, **options)
  File "/Users/noopy/django-airbnb-clone/lists/management/commands/seed_lists.py", line 60, in handle
    created = seeder.execute()
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django_seed/seeder.py", line 157, in execute
    entity = self.entities[klass].execute(using, inserted_entities)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django_seed/seeder.py", line 101, in execute
    obj = manager.create(**faker_data)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/query.py", line 433, in create
    obj.save(force_insert=True, using=self.db)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/base.py", line 745, in save
    self.save_base(using=using, force_insert=force_insert,
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/base.py", line 782, in save_base
    updated = self._save_table(
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/base.py", line 887, in _save_table
    results = self._do_insert(cls._base_manager, using, fields, returning_fields, raw)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/base.py", line 924, in _do_insert
    return manager._insert(
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/query.py", line 1204, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1384, in execute_sql
    cursor.execute(sql, params)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 100, in execute
    return super().execute(sql, params)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 77, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
  File "/Users/noopy/.local/share/virtualenvs/django-airbnb-clone-AcLC9Tzu/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 396, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: UNIQUE constraint failed: lists_list.user_id