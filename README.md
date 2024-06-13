<h1> Voting Pole App </h1>

-->         Create virtual environment

    virtualenv vote-nv

-->         Activae virtual environment

    source vote-nv/bin/activate

-->         Download the requirements

    pip install -r requirement.txt

-->         Run commands

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

