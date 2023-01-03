# URL_Shortener

## Project Requirements
### Required 
- [x] On the main page of the service, provide a web interface by which a user can shorten a URL;
- [x] If a user visits the short URL, they must receive a temporary HTTP redirect to the long URL;
- [x] Attempt to optimize the speed at which the URL is resolved to the best of your ability;
- [x] All the short URLs must be reasonably short and of the same length;
- [x] Given a short URL, it must be impossible to identify the long URL, when the short URL was generated, or which user generated it, or any other metadata in any other way than via the service API;
- [x] It must be impossible to easily identify which of the two given short URLs was generated earlier;
- [x] If the same long URL is shortened the second time, it must produce a different short URL;
- [x] Provide a Readme file with instructions on how to run the service;
- [x] Provide tests covering the core functionality;

### Optional 
- [ ] Provide an admin interface for the user which allows to deactivate or permanently delete any of the URLs they have shortened;
- [x] Record the click statistics for each short URLs that the user has created and display it in the admin interface: time; IP address; HTTP Referer;
- [x] Expiration time: automatically deactivate the URL at a given time (configured per URL in the admin interface);
- [x] Limit maximum number of clicks on URL: automatically deactivate the URL after the limit is reached;
- [x] Allow to run the service with docker-compose up command;
- [ ] Provide a benchmark to showcase the speed of redirecting from short to long URLs.


## Steps to run the website 

#### 1. Build the docker container
```bash
docker-compose build
```

##### 2. Make migrations

```bash
docker-compose run --rm url_shortener python manage.py makemigrations
```

##### 3. Migrate

```bash
docker-compose run --rm url_shortener python manage.py migrate
```

##### 4. Run the server

```bash
docker-compose up
```
