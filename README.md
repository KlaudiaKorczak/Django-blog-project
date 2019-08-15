# Django project
    This is my first Django app for my future digital art portfolio and blog.
     This website will be hosted on Cloud Server after completing and fine-tuning the project and preparing sufficient number of art works.

Used:
- Free Bootstrap template "Clean Blog"
- Database - SQLite


## Installation and run:

1) Clone this repository
type these commands from project directory:
1) Prepare venv (for Windows)

    'python -m venv venv'
    'venv\Scripts\activate'
    'pip install -r requirements.txt'

    To exit venv: 'deactivate'

2) create secret key, copy this key from new secretkey.txt file and paste it into the settings.py -> SECRET_KEY

    'python manage.py generate_secret_key'

3) Load data and make db migration
    'python manage.py migrate'
    'python manage.py load_data'

4) Run Django project
type these commands from project directory:

    '''bash
    python manage.py runserver
    '''

5) Go to http://localhost:8000/

## Features
