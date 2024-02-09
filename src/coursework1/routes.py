from flask import current_app as app
from coursework1 import db
from coursework1.models import YR2011, YR2021
from flask import request
from coursework1.schemas import YR2011Schema, YR2021Schema


app.app_context()
@app.route('/')
def hello():
  return f"Landing Page"


# Flask-Marshmallow Schemas
YR2011_schema = YR2011Schema(many=True)
#YR2011_schema = YR2011Schema()
YR2021_schema = YR2021Schema(many=True)
#YR2021_schema = YR2021Schema()


# Use Flask shortcut methods for each HTTP method `.get`, `.post`, `.delete`, `.patch`, `.put`
@app.get("/yr2011")
def get_yr2011():
    """Returns a list of NOC region codes and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all = db.session.execute(db.select(YR2011)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = YR2011_schema.dump(all)
    # Return the data
    return result

# Use Flask shortcut methods for each HTTP method `.get`, `.post`, `.delete`, `.patch`, `.put`
@app.get("/yr2021")
def get_yr2021():
    """Returns a list of NOC region codes and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all = db.session.execute(db.select(YR2021)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = YR2021_schema.dump(all)
    # Return the data
    return result


@app.get("/yr2011/<yr2011_area>")
def get_yr2011_area(yr2011_area):
    """ Returns the event with the given id JSON.

    :param event_id: The id of the event to return
    :param type event_id: int
    :returns: JSON
    """
    event = db.session.execute(
        db.select(YR2011).filter_by(area=yr2011_area)).scalars()
    return YR2011_schema.dump(event)

@app.get("/yr2021/<yr2021_area>")
def get_yr2021_area(yr2021_area):
    """ Returns the event with the given id JSON.

    :param event_id: The id of the event to return
    :param type event_id: int
    :returns: JSON
    """
    event = db.session.execute(
        db.select(YR2021).filter_by(area=yr2021_area)).scalars()
    return YR2021_schema.dump(event)


@app.post('/newarea2011')
def new_area2011():
    """ Adds a new event.
    
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
    """ Adds a new event.
    
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
    """ Deletes an event.
    
    Gets the event from the database and deletes it.

    :returns: JSON"""
    event = db.session.execute(
        db.select(YR2011).filter_by(area=yr2011area)).scalar_one_or_none()
    db.session.delete(event)
    db.session.commit()
    return {"message": f"Deleted area: {yr2011area}"}

@app.delete('/deletearea2021/<yr2021area>')
def delete_yr2021(yr2021area):
    """ Deletes an event.
    
    Gets the event from the database and deletes it.

    :returns: JSON"""
    event = db.session.execute(
        db.select(YR2021).filter_by(area=yr2021area)).scalar_one_or_none()
    db.session.delete(event)
    db.session.commit()
    return {"message": f"Deleted area: {yr2021area}"}