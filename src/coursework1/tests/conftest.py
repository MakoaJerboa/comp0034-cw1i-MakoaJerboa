import os
from pathlib import Path
import pytest
from coursework1 import create_app

try:
    # clean up / reset resources
    # Delete the test database
    db_path = Path(__file__).parent.parent.parent.joinpath('instance', 'coursework1_testdb.sqlite')
    os.unlink(db_path)
except FileNotFoundError:
    pass


@pytest.fixture(scope='module')
def app():
    """Fixture that creates a test app.

    The app is created with test config parameters that include a temporary database. The app is created once for
    each test module.

    Returns:
        app A Flask app with a test config
    """
    # Location for the temporary testing database
    db_path = Path(__file__).parent.parent.parent.joinpath('instance', 'coursework1_testdb.sqlite')
    test_cfg = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(db_path),
    }
    app = create_app(test_config=test_cfg)

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()