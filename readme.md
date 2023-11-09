
# movie_app



## Run Locally

Clone the project

```bash
  git clone https://github.com/Sanjay309/movie_app.git
```

Go to the project directory

```bash
  cd movie
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Migrate the models

```bash
  python manage.py makemigrations; python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

Check all available API in swagger doc - http://localhost:8000/redoc/

    /doc (Our nice pretty Swagger UI view of API doc)
    /redoc (A pretty Redoc view of API doc)


