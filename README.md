# Django API Implementation


### Local SuperUser
SuperUserEmail - hero@djangousers.com
SuperUserPassword - herokun123

### Local Database

**Used Postgres as Database**

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_recipe',
        'USER': 'django',
        'PASSWORD': 'djangoapprecipe',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

### To Start Server

*Run* `python manage.py runserver`

### To Test

*Run* `python manage.py test`