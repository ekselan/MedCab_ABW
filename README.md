# MedCab_ABW

## Installation for Dependencies
Flask, Flask-Cors, Psycopg2, Gunicorn, Requests, Dotenv
- pipenv
```sh
pipenv install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv scikit-learn pandas
```
- conda
```sh
pip install Flask flask-cors psycopg2-binary gunicorn requests python-dotenv scikit-learn pandas
```
- PostgreSQL Database Connection
Example of format to place credentials inside a .env file:
```py
DB_USER="___________"
DB_NAME="___________"
DB_PASSWORD="___________"
DB_HOST="___________"
```
---

## Running the app locally using Flask  
**In a terminal:**  
Mac/Linux:  
`FLASK_APP=MedCab flask run`  
Windows:  
`export FLASK_APP=MedCab` (set env var)  
`flask run`

---