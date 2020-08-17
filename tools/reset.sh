read -p "Are you sure? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # do dangerous stuff
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    rm db.sqlite3
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
fi
