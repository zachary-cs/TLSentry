from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'm4Vmu+12giu8GvmSMK/POt88CIi9tkW2Q+Sn1v8DOLSp+5GoMCjcj7w0KuapaC+EMECZA1TYD9lBdoFqNjNcQA=='


    # Define blueprint views here
    from .home import home
    from .snippets import snips
    from .scanner import scanner
    from .certs import certs

    # Register them with the app
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(snips, url_prefix='/snips')
    app.register_blueprint(scanner, url_prefix='/scanner')
    app.register_blueprint(certs, url_prefix='/certs')

    return app