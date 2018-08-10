# Django Vue Template 🐍✌️

![Vue Logo](/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/src/assets/logo-django.png "Django Logo")

This template is a minimal example for structuring an application using VueJs and Django (RestFramework).

The goal is to let Vue + Vue Cli handle the frontend and asset bundling,
and use Django + Rest Framework to manage a Data Models, API, and Static files.

Vue Cli and Django Project template are kept as close as possible to their
original state, with the exception of some configuration that is critical
to the integration of the two frameworks.

### Demo

[Live Demo](https://django-vue-template-demo.herokuapp.com/)

### Includes

* Django
* Django Restframework
* Django Whitenoise
* Gunicorn
* Vue Cli 3
* Vue Router
* Configuration for Heroku Deployment


## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv

## Setup Template

```
$ git clone https://www.github.com/gtalarico/django-vue
$ cd django-vue
```

Setup
```
$ yarn install
$ pipenv install
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```

From another tab in the same directory:

```
$ yarn serve
```

The Vuejs template will be served from `localhost:8080` and the Django Api
and static files will be served from `localhost:8000`.

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in `vue.config.js` is used to router the requests
back to django's Api.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```


## Deploy

* Set `ALLOWED_HOSTS` on `project.settings.production.py`

### Heroku Server

```
$ heroku apps:create django-vue-template-demo
$ heroku git:remote --app django-vue-template-demo
$ heroku buildpacks:add --index 1 heroku/nodejs
$ heroku buildpacks:add --index 2 heroku/python
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=project.settings.prod

$ git push heroku
```

Since nodejs buidlpack was added, heroku will handle install for all the dependencies from the `packages.json` file. 
It will then trigger the `postinstall` command which calls `yarn build`. 
This will create the bundled `dist` folder which will be served by whitenoise. 

The python buildpack will detect the `pipfile` and install all the python dependencies. 

## Static Assets

See `settings.dev` and `vue.config.js` for notes on static assets strategy.

This template implements the approach suggested by Whitenoise Django.
For more details see [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/django.html)

It uses Django Whitenoise to serve all static files and Vue bundled files at `/static/`.
While it might seem inefficient, the issue is immediately solved by adding a CDN
with Cloudfront or similar.
Use `vue.config.js` > `baseUrl` option to set point all your assets to the CDN,
and then set your CDN's origin back to your domains `/static` url.

Whitenoise will serve static files to your CDN once, but then those assets are cached
and served directly by the CDN.

This allows for an extremely simple setup without the need for a separate static server.
