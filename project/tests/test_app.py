import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app():
    return import_app("project.app")


def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("h1")


def test_visualization_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("#visualization")


def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    assert dash_duo.find_element("#region-picker")
