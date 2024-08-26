# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from datetime import datetime
# app = Flask(__name__)
# db = SQLAlchemy()
# migrate = Migrate(app,db)


# def create_app(config_class='config.Config'):
    
#     app.config.from_object(config_class)
    
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     from app.main.routes import main
#     app.register_blueprint(main)
#     from . import models
#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
db = SQLAlchemy()
# migrate = Migrate()
migrate = Migrate(app, db)
def create_app():
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    from app.main.routes import main
    migrate.init_app(app, db)
    app.register_blueprint(main)
    with app.app_context():
        # Import parts of our application
        from . import models

    return app
