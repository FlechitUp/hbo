Intall packages from requirements:
    pip install -r requirements.txt

Activate virtual environment:
    source activate DjangoProject

Run server:
    python manage.py runserver

    
-----------
Create DB
$sudo -i -u postgres psql
postgres=# CREATE USER “your_username” WITH PASSWORD “your_pass”;
postgres=# CREATE DATABASE teste_django WITH OWNER your_username;

python manage.py makemigrations
python manage.py migrate


user: xime
pass: root
----------------
ADMIM

user: ximenAs
pass: 123456A.
