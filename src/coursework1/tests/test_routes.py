def test_get_yr2011_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /yr2011
    THEN the status code should be 200
    """
    response = client.get("/yr2011")
    assert response.status_code == 200


def test_get_yr2011_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the areas
    WHEN a request is made to /yr2011
    THEN the response should contain json
    AND a JSON object for Barking should be in the json
    """
    response = client.get("/yr2011")
    assert response.headers["Content-Type"] == "application/json"
    Barking = {"area": "Barking and Dagenham",
    "fifteen_or_less": 6745,
    "forty_nine_or_more": 7131,
    "sixteen_to_thirty": 15078,
    "thirty_one_to_forty_eight": 46263,
    "total": 75217}
    assert Barking in response.json


def test_get_yr2021_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /yr2021
    THEN the status code should be 200
    """
    response = client.get("/yr2021")
    assert response.status_code == 200

def test_get_yr2021_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the areas
    WHEN a request is made to /yr2021
    THEN the response should contain json
    AND a JSON object for Barking should be in the json
    """
    response = client.get("/yr2021")
    assert response.headers["Content-Type"] == "application/json"
    Barking = {"area": "Barking and Dagenham",
    "fifteen_or_less": 10781,
    "forty_nine_or_more": 8215,
    "sixteen_to_thirty": 20099,
    "thirty_one_to_forty_eight": 55490,
    "total": 94585}
    assert Barking in response.json


def test_get_area_yr2011_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /yr2011/Barnet
    THEN the status code should be 200
    """
    response = client.get("/yr2011/Barnet")
    assert response.status_code == 200

def test_get_area_yr2011_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the Barnet area
    WHEN a request is made to /regions/Barnet
    THEN the response should contain json
    AND a JSON object for Barnet should be identical to
    the response JSON
    """
    response = client.get("/yr2011/Barnet")
    assert response.headers["Content-Type"] == "application/json"
    Barnet = {"area": "Barnet",
    "fifteen_or_less": 17500,
    "forty_nine_or_more": 26362,
    "sixteen_to_thirty": 31467,
    "thirty_one_to_forty_eight": 95329,
    "total": 170658}
    assert Barnet in response.json


def test_get_area_yr2021_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /yr2021/Barnet
    THEN the status code should be 200
    """
    response = client.get("/yr2021/Barnet")
    assert response.status_code == 200

def test_get_area_yr2021_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the regions
    WHEN a request is made to /yr2021/Barnet
    THEN the response should contain json
    AND a JSON object for Barnet should be in the json
    """
    response = client.get("/yr2021/Barnet")
    assert response.headers["Content-Type"] == "application/json"
    Barnet = {"area": "Barnet",
    "fifteen_or_less": 23744,
    "forty_nine_or_more": 24725,
    "sixteen_to_thirty": 35920,
    "thirty_one_to_forty_eight": 101773,
    "total": 186162}
    assert Barnet in response.json


def test_post_yr2011(client):
    """
    GIVEN a Flask test client
    AND valid JSON for a new area
    WHEN a POST request is made to /newarea2011
    THEN the response status_code should be 200
    """
    # JSON to create a new area
    newarea_json = [{
    "area": "test",
    "fifteen_or_less": 0,
    "forty_nine_or_more": 1,
    "sixteen_to_thirty": 2,
    "thirty_one_to_forty_eight": 3,
    "total": 10}]
    # pass the JSON in the HTTP POST request
    response = client.post(
        "/newarea2011",
        json=newarea_json,
        content_type="application/json",
    )
    # 200 is the HTTP status code for a successful POST or PUT request
    assert response.status_code == 200


def test_post_yr2021(client):
    """
    GIVEN a Flask test client
    AND valid JSON for a new area
    WHEN a POST request is made to /newarea2021
    THEN the response status_code should be 200
    """
    # JSON to create a new region
    newarea_json = [{
    "area": "test",
    "fifteen_or_less": 0,
    "forty_nine_or_more": 1,
    "sixteen_to_thirty": 2,
    "thirty_one_to_forty_eight": 3,
    "total": 10}]
    # pass the JSON in the HTTP POST request
    response = client.post(
        "/newarea2021",
        json=newarea_json,
        content_type="application/json",
    )
    # 200 is the HTTP status code for a successful POST or PUT request
    assert response.status_code == 200


def test_delete_yr2011(client):
    """
    GIVEN a Flask test client
    AND a region exists in the database
    WHEN a DELETE request is made to /deletearea2011/Brent
    THEN the response status_code should be 200
    """
    response = client.delete("/deletearea2011/Brent")
    assert response.status_code == 200

def test_delete2_yr2011(client):
    """
    GIVEN a Flask test client
    AND a region exists in the database
    WHEN a DELETE request is made to /deletearea2011/Bromley
    THEN the response status_code should be 200
    """
    response = client.delete("/deletearea2011/Bromley")
    assert response.status_code == 200


def test_delete_yr2021(client):
    """
    GIVEN a Flask test client
    AND a region exists in the database
    WHEN a DELETE request is made to /deletearea2021/Brent
    THEN the response status_code should be 200
    """
    response = client.delete("/deletearea2021/Brent")
    assert response.status_code == 200

def test_delete_yr2021(client):
    """
    GIVEN a Flask test client
    AND a region exists in the database
    WHEN a DELETE request is made to /deletearea2021/Bromley
    THEN the response status_code should be 200
    """
    response = client.delete("/deletearea2021/Bromley")
    assert response.status_code == 200