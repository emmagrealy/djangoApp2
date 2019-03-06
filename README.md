## Django Tutorial

### Setting up enviornment
``pipenv install django==2.1``, entered after Z:\3rdYear\WebDev\DjangoTutorial>

- let this load fully then enter , `` pipenv shell``

- if i am to reload a project i only need: 
change to mysite, then ``pipenv shell``

- ``cd mysite``
- check if django is available by running: ``py manage.py``


- HOW TO RUN THE SERVER:  ``py manage.py runserver``
- OPENING WEB PAGE: localhost:8000 in browser

- a new directory is a new folder!!

- ``pipenv install Pillow`` for uploading image 

- database info:
    - ``py manage.py makemigrations``
    - ``py manage.py migrate``

- ``{{ user.username }}`` accesses the name of the user logged in