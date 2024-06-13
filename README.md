<h1> Voting Pole App </h1>

-->         Create virtual environment

    virtualenv vote-nv

-->         Activae virtual environment

    source vote-nv/bin/activate

-->         Download the requirements

    pip install -r requirement.txt

-->         Create super user 
            It is officer login ID

    python manage.py createsuperuser

-->         Run commands

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


