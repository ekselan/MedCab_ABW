from flask import Blueprint
from medcab_app.routes.services import fetch_data, fetch_strains, fetch_top

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return "Hello, we're here to help."


@home_routes.route("/strains")
def strains():
    query = '''
    SELECT id, strain, rating
    FROM medcab
    '''
    return fetch_strains(query)


@home_routes.route("/recx")
def recommendations():
    return "This will list recommendations."


@home_routes.route("/data")
def data():
    query = """
    SELECT *
    FROM medcab
    """
    return fetch_data(query)


@home_routes.route("/toptenrating")
def toprating():
    query = """
    SELECT strain
    FROM medcab
    where rating >= 5.0
    ORDER BY LENGTH(medical) DESC
    LIMIT 10
    """
    return fetch_top(query)


@home_routes.route("/toptenflavor")
def topflavor():
    query = """
    SELECT strain
    FROM medcab
    ORDER BY LENGTH(flavors) DESC
    LIMIT 10
    """
    return fetch_top(query)