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

    ```
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

    To exit venv: `deactivate`

2) Create secret key

    ```python manage.py generate_secret_key```
 Copy this key from new secretkey.txt file and paste it into Your new secret file `secret_settings.py` as `SECRET_KEY`. Store this with `EMAIL` and `PASSWORD` for the contact possibility, in the secret file in the main project drectory.

3) Load data and make db migration
    ```
    python manage.py migrate
    python manage.py load_data
    ```
4) Run Django project
type these commands from project directory:

    ```
    python manage.py runserver
    ```

5) Go to (http://localhost:8000/)

## Features
- Portfolio page with possibility of adding comments
- Contact through the email
- Simple polling
