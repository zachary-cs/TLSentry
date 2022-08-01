from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'm4Vmu+12giu8GvmSMK/POt88CIi9tkW2Q+Sn1v8DOLSp+5GoMCjcj7w0KuapaC+EMECZA1TYD9lBdoFqNjNcQA=='


    # Define blueprint views here
    from .home import home


    # Register them with the app
    app.register_blueprint(home, url_prefix='/')

    return app