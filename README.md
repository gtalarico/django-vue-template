# Django Vue Template 🐍✌️

This template is a minimal example for structuring a VueJs + Django Rest Framework.

The goal is to let Vue + Vue Cli handle the frontend and asset bundling,
and use Django + Rest Framework to manage a Rest API + Data Models.

Vue Cli and Django Project template are kept as close as possible to their
original state, with the exception of some configuration that is critical
to the integration of the two frameworks.

### Demo

https://django-vue-template-demo.herokuapp.com/

## Prerequisites

Before getting started you should have the following installed on your computer

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv

## Setup Template Locally

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
will be served form `localhost:8000`.

The dual dev server setup allows you to take advantage of
webpack's development server with hot module reload.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build build the Vue app first

```
$ yarn build
$ python manage.py runserver
```



## Deploy

* Set `ALLOWED_HOSTS` on `project.settings.production.py`

A Heroku deploymnet is preconfigured:

```
$ heroku apps:create django-vue-template-demo
$ heroku buildpacks:add --index 1 heroku/nodejs
$ heroku buildpacks:add --index 2 heroku/python
$ heroku git:remote --app django-vue-template-demo
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set YARN_PRODUCTION=true
$ heroku config:set DJANGO_SETTINGS_MODULE=project.settings.prod

$ git push heroku
```

## Static Assets

See `settings.prod` and `vue.config.js` for comments on static assets strategy.

This template is configured for development, but not a lot is needed to have a decent
production setup.

The strategy we take is to use Django Whitenoise to serve all static files at `/static/`.

This may seem inefficient for a production server, but that's immediately solved
by adding a CDN.
Create CDN distribution with Cloudfront or similar, configure the `vue.config.js` `baseUrl` options to set your point to the CDN, and set your CDN's origin back to your domains `/static` url.

The CDN will fetch assets, cache, and then distribute it for you.
This allows for a extremely simple setup without the need to keep a separate static server or
upload static assets.

For more details see [WhiteNoise Docs](http://whitenoise.evans.io/en/stable/django.html)

