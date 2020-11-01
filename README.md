Docker-compose version
====

First run:
===
```docker-compose run web python manage.py migrate```
```docker-compose run web python manage.py createsuperuser```

For the rest:
===
```docker-compose up --build```