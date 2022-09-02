# PokeSafe

A live version of the project is accessible at [pokesafe.herokuapp.com](https://pokesafe.herokuapp.com/).
(Note that — because of free Dynos — it might take a little while to load if the app is asleep.)

## Quickstart

```shell
docker-compose up -d
docker-compose exec web python manage.py migrate
```

## Development

1. (recommended) Set up a virtual environment:
   ```shell
   python -m venv venv
   source venv/bin/activate
   ```
2. Install and activate pre-commits:
   ```shell
   pip install -r requirements-dev.txt
   pre-commit install
   pre-commit install --hook-type commit-msg  # require explicit install, as per https://github.com/compilerla/conventional-pre-commit
   ```


Run tests:

```shell
docker-compose exec web python manage.py test
```

Update model

```shell
docker-compose up -d
docker-compose exec web python manage.py makemigrations pokesafe
```
