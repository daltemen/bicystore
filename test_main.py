import pytest


@pytest.fixture
def app():
    import main
    main.app.testing = True
    return main.app.test_client()


def test_hello_world():
    assert True is True

# def test_get_brakes(app, testbed):
#     r = app.get('/bicystore/api/v1/brakes')
#     assert r.status_code == 200
#
#
# def test_post_brakes(app, testbed):
#     r = app.post('/bicystore/api/v1/brakes')
#     assert r.status_code == 201
