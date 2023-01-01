```bash
docker-compose run --rm url_shortener python manage.py makemigrations
docker-compose run --rm url_shortener python manage.py migrate
docker-compose run --rm url_shortener python manage.py createsuperuser
docker-compose up
```
