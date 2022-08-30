need to add env vars:
DATABASE_NAME
...

## развернуть локально:
pip install -r requirements

python manage.py migrate

python manage.py runserver

...

## развернуть через контейнер:
```shell
docker-compose up --build
```
предварительно должен быть установлен postgres

