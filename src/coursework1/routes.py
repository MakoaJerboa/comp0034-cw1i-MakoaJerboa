from flask import current_app as app
from coursework1 import db
from coursework1.models import YR2011, YR2021
from flask import request, url_for
from coursework1.schemas import YR2011Schema, YR2021Schema


# Defines a route for the default page which links to the others
app.app_context()
@app.get('/')
def landing_page():
    """Returns the landing page with a hyperlink to the /yr2011 route."""
    return f"<h1>Landing Page</h1>\
    <a href='{url_for('get_yr2011')}'>See data from 2011</a>\
    <a href='{url_for('get_yr2021')}'>See data from 2021</a>\
    <br>\
    <body>You can also see data for a specific year and area by going to /yr(2011 or 2021)/(name of area) without brackets</body>"


# Flask-Marshmallow Schemas
YR2011_schema = YR2011Schema(many=True)
YR2021_schema = YR2021Schema(many=True)


# Used Flask shortcut methods for each GET HTTP method `.get`, `.post` and `.delete`
@app.get("/yr2011")
def get_yr2011():
    """Returns for all data collected in 2011 in JSON."""
    # Select all the areas using Flask-SQLAlchemy
    all = db.session.execute(db.select(YR2011)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = YR2011_schema.dump(all)
    # Return the data
    return result

@app.get("/yr2021")
def get_yr2021():
    """Returns for all data collected in 2021 in JSON."""
    # Select all the area using Flask-SQLAlchemy
    all = db.session.execute(db.select(YR2021)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = YR2021_schema.dump(all)
    # Return the data
    return result


@app.get("/yr2011/<yr2011_area>")
def get_yr2011_area(yr2011_area):
    """ Returns the data for the given area name for 2011 in JSON.

    :param yr2011_area: The name of the area to return data for
    :param type yr2011_area: str
    :returns: JSON
    """
    event = db.session.execute(
        db.select(YR2011).filter_by(area=yr2011_area)).scalars()
    return YR2011_schema.dump(event)

@app.get("/yr2021/<yr2021_area>")
def get_yr2021_area(yr2021_area):
    """ Returns the data for the given area name for 2021 in JSON.

    :param yr2021_area: The name of the area to return data for
    :param type yr2021_area: str
    :returns: JSON
    """
    event = db.session.execute(
        db.select(YR2021).filter_by(area=yr2021_area)).scalars()
    return YR2021_schema.dump(event)


@app.post('/newarea2011')
def new_area2011():
    """ Adds data for a new area for 2011.
    
    Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
    event_schema.load()

    :returns: JSON"""
    YR2011_json = request.get_json()
    newarea2011 = YR2011_schema.load(YR2011_json)
    for parameter in newarea2011:
        db.session.add(parameter)
    db.session.commit()
    return {"message": f"Added new area: {newarea2011}"}

@app.post('/newarea2021')
def new_area2021():
    """ Adds data for a new area for 2011.
    
    Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
    event_schema.load()

    :returns: JSON"""
    YR2021_json = request.get_json()
    newarea2021 = YR2021_schema.load(YR2021_json)
    for parameter in newarea2021:
        db.session.add(parameter)
    db.session.commit()
    return {"message": f"Added new area: {newarea2021}"}


@app.delete('/deletearea2011/<yr2011area>')
def delete_yr2011(yr2011area):
    """ Deletes data for an area for 2011.
    
    Gets the area data from the database and deletes it.

    :returns: JSON"""
    event = db.session.execute(
        db.select(YR2011).filter_by(area=yr2011area)).scalar_one_or_none()
    db.session.delete(event)
    db.session.commit()
    return {"message": f"Deleted area: {yr2011area}"}

@app.delete('/deletearea2021/<yr2021area>')
def delete_yr2021(yr2021area):
    """ Deletes data for an area for 2021.
    
    Gets the area data from the database and deletes it.

    :returns: JSON"""
    event = db.session.execute(
        db.select(YR2021).filter_by(area=yr2021area)).scalar_one_or_none()
    db.session.delete(event)
    db.session.commit()
    return {"message": f"Deleted area: {yr2021area}"}