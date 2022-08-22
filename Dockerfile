FROM kennethreitz/pipenv:latest

# Sets the working directory to /code in the docker ubuntu image
WORKDIR /code

COPY Pipfile /code
COPY Pipfile.lock /code

# install python project dependencies
RUN pipenv install

CMD ["bash", "./startup.sh"]
