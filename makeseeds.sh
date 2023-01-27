
echo "creating pets/seeds.json"
python manage.py dumpdata pets --output pets/seeds.json --indent=2;

echo "creating lifespans/seeds.json"
python manage.py dumpdata lifespans --output lifespans/seeds.json --indent=2;

echo "creating environments/seeds.json"
python manage.py dumpdata environements --output environements/seeds.json --indent=2;

echo "creating comments/seeds.json"
python manage.py dumpdata comments --output comments/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;