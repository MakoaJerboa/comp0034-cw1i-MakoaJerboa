from coursework1.models import YR2011, YR2021
from coursework1 import db, ma


class YR2011Schema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of an event class. Inherits all the attributes from the 2011 class."""

    class Meta:
        model = YR2011
        #include_fk = True
        load_instance = True
        sqla_session = db.session
        #include_relationships = True

class YR2021Schema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of an event class. Inherits all the attributes from the 2021 class."""

    class Meta:
        model = YR2021
        load_instance = True
        sqla_session = db.session