import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_object(DevelopmentConfig)

    app.config.from_mapping(
        ENV='development',  # 'production'
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'testdb.sqlite'),
        SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return '<h2>Hello, World!</h2>'

    return app
