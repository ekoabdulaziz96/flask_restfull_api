## Note:
this project is create and inspire from flask cookiecuter: https://github.com/cookiecutter-flask/cookiecutter-flask
<br> this project goal is to build flask proect for RESTfull API 
<br> using python 3.8 
<br> using flask_sqlalchemy, flask_migrate, 

## install requirements lib python

```bash
# if using virtual env, create your virtualenv and activate
pip install -r ./requirements.txt
```

## Env Variabel

```bash
# note: the code below is using powershell
cd ./flask_restfull_api
$env:SECRET_KEY='secret_key'
$env:FLASK_APP="server.py"
$env:FLASK_ENV="development"
$env:DATABASE_URL="url_database"
ex: $env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:5432/postgres"
```

## Database
```bash
# init flask migrate file location
flask db init -d 'models/migrations'

# make migrate file, for any change in your models
flask db migrate -d 'models/migrations' -m 'message'
# ex:
flask db migrate -d 'models/migrations' -m 'add table user'

# execute your change in db
flask db upgrade -d 'models/migrations'
```

## Run Project
```bash
# init flask migrate file location
flask run
```