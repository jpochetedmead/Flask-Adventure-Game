from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    @app.route('/')
    def index():
        return 'Flask Heroku Demo'

    # a simple page that says hello
    @app.route('/hello')
    def hello_world():
        return 'Hello, World!'

    return app
