"""Testing fixtures for coding tasks"""
import pytest

@pytest.fixture
def valid_line():
    return "03/11/21 08:51:01 INFO    :.main: *************** RSVP Agent started ***************"

@pytest.fixture
def bad_error_code():
    return "03/11/21 08:51:01 BIG    :.main: *************** RSVP Agent started ***************"

@pytest.fixture
def invalid_time():
    return "03/11/21 08:5: INFO    :.main: *************** RSVP Agent started ***************"

@pytest.fixture
def missing_time():
    return "WARNING    :.main: *************** RSVP Agent started ***************"

@pytest.fixture
def missing_message():
    return "03/11/21 08:51:01 INFO    "

@pytest.fixture
def court_list():
    return [{
        "name" : "test_name",
        "distance": "test_dist",
        "types": ["test_type"],
        "dx_number" : "test_num"
        }]

@pytest.fixture
def court_list_types():
    return [{
        "name" : "test_name",
        "distance": 5,
        "types": ["test_type", "non-matching"],
        "dx_number" : "test_num"
        },
        {
        "name" : "test_name",
        "distance": 4,
        "types": ["not_matching"],
        "dx_number" : "test_num"}]

@pytest.fixture
def person_string():
    return "Paul Blart,NR162HE,Crown Court"

@pytest.fixture
def person_list():
    return ["Paul Blart", "NR162HE","Crown Court"]

@pytest.fixture
def close_court():
    return {
        "name" : "test_name",
        "distance": 11.03,
        "types": ["test_type"],
        "dx_number" : "test_num"
        }

@pytest.fixture
def court_missing_key():
    return {
        "name" : "test_name",
        "distance": 11.03,
        }

@pytest.fixture
def full_test_courts():
    return [{
        "name" : "Test Crown Court",
        "distance": 11.03,
        "types": ["Crown Court"],
        "dx_number" : "Test dx"
        }]