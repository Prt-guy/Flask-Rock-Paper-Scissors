# adapted from: https://github.com/prof-rossetti/web-app-starter-flask/blob/master/web_app/__init__.py

import os

from dotenv import load_dotenv
from flask import Flask

from web_app.routes import game_routes

def create_app():
    load_dotenv()

    app_env = os.environ.get("FLASK_ENV", "development") # set to "production" in the production environment
    secret_key = os.environ.get("SECRET_KEY", "my super secret") # overwrite this in the production environment
    testing = False # True if app_env == "test" else False

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, TESTING=testing)

    app.register_blueprint(game_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True) # debug mode allows you to see printed content in development environment
