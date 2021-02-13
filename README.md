# Crypto Django

This is an application that will allow the user to enter sensitive data.
That data will be encrypted using the django-pgcrypto package.

[Link to django-pgcrypto documentation.](https://github.com/dcwatson/django-pgcrypto)

## Dependencies

[Python 3.7](https://www.python.org/downloads/)  
[pip](https://pip.pypa.io/en/stable/installing/)  
[Django](https://docs.djangoproject.com/en/3.1/)  
[Postgres](https://www.postgresql.org/)  

## Docker and docker-compose

1. [Install Docker](https://docs.docker.com/get-docker/)  

If you use Linux and need to use `sudo` before `docker-compose` command just follow step below:

manage Docker as a non-root user:  [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)  

2. [Install docker-compose](https://docs.docker.com/compose/install/)  

3. Commands:

If you want to build and run containers - you can do it in two ways:

Build and run containers:

`docker-compose up -d --build`

Or

Build the image:  
`docker-compose build`

Fire up cointainers:  
`docker-compose up`

Or fire up containers in detached mode:  
`docker-compose up -d`
