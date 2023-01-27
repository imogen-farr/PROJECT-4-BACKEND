echo "dropping database django-pets"
dropdb django-pets

echo "creating database django-pets"
createdb django-pets

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting environments"
python manage.py loaddata environments/seeds.json

echo "inserting lifespans"
python manage.py loaddata lifespans/seeds.json

echo "inserting pets"
python manage.py loaddata pets/seeds.json

echo "inserting comments"
python manage.py loaddata comments/seeds.json