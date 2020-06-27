from flask import Flask
from flask_cors import CORS


from MedCab.alt_routes.home_routes import home_routes  # connection, cursor
from MedCab.alt_routes.model_routes import model_routes


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.register_blueprint(home_routes)
    app.register_blueprint(model_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
