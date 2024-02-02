import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)
    # configure the Flask app (see later notes on how to generate your own SECRET_KEY)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # Set the location of the database file called paralympics.sqlite which will be in the app's instance folder
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path, 'coursework1.sqlite'),  
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

     # Initialise Flask with the SQLAlchemy database extension
    db.init_app(app)

    # Models are defined in the models module, so you must import them before calling create_all, otherwise SQLAlchemy
    # will not know about them.
    from coursework1.models import Hours, Area, Total
    # Create the tables in the database
    # create_all does not update tables if they are already in the database.

    with app.app_context():
        db.create_all()
        # Register the routes with the app in the context
        add_data_from_csv()
        from coursework1 import routes

    return app

import csv
from pathlib import Path

def add_data_from_csv():
    """Adds data to the database if it does not already exist."""

    # Add import here and not at the top of the file to avoid circular import issues
    from coursework1.models import Area, Total, Hours
    
    # If there are no regions in the database, then add them
    first_area = db.session.execute(db.select(Area)).first()
    if not first_area:
        print("Start adding region data to the database")
        area_file = Path(__file__).parent.joinpath("data", "dataset_prepared_2011.csv")
        with open(area_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # row[0] is the first column, row[1] is the second column
                a = Area(area=row[1])
                db.session.add(a)
            db.session.commit()
    

    # If there are no Events, then add them
    file = Path(__file__).parent.joinpath("data", "dataset_prepared_2011.csv")
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            # row[0] is the first column, row[1] is the second column etc
            # For int data types, if there is no value, set to None rather than ''
            t = Total(total=row[2],)
            db.session.add(t)
        db.session.commit()

    # If there are no Events, then add them
    file = Path(__file__).parent.joinpath("data", "dataset_prepared_2011.csv")
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            # row[0] is the first column, row[1] is the second column etc
            # For int data types, if there is no value, set to None rather than ''
            h = Hours(total=row[2],)
            db.session.add(h)
        db.session.commit()
