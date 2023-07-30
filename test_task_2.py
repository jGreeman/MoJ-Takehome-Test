"""Testing task 2 functions"""
import pytest
import requests
from unittest.mock import patch
from test_2 import (find_courts, find_correct_court_type, 
                    get_min_distance_of_court, person_output_dict, main_routine)
from conftest import (court_list, court_list_types, person_string,
                    close_court, court_missing_key, person_list, full_test_courts)



class TestFindCourts:
    """Tests for the find_courts function"""
        
    def test_find_courts_with_postcode(self, requests_mock):
        """Tests that find_courts sends a get request to the API with postcode as query parameter"""
        requests_mock.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode=SG88ST",
                          status_code=200, json = {})
                                
        courts = find_courts("SG88ST")

        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    def test_find_courts_returns_list_dict(self, requests_mock, court_list):
        """Tests that find_courts returns a list of dicts if receiving a valid response from the API"""
        requests_mock.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode=SG88ST",
                          status_code=200, json = court_list)
        
        courts = find_courts("SG88ST")
        assert isinstance(courts, list)
        assert all(isinstance(court, dict) for court in courts)

    def test_find_courts_correct_keys(self, requests_mock, court_list):
        """Tests that find_courts returns a list of dicts if receiving a valid response from the API"""
        requests_mock.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode=SG88ST",
                          status_code=200, json = court_list)
        
        court = find_courts("SG88ST")[0]
        assert all(key in court for key in ["dx_number", "types", "name", "distance"])


    def test_raises_error(self, requests_mock):
        """Tests that an error is raised if receiving a 404 HTTP response"""
        requests_mock.get(f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode=SG88ST",
                          status_code=404)
        with pytest.raises(requests.HTTPError) as err:
            find_courts("SG88ST")


class TestFindCorrectCourtType:
    """Tests for the find_correct_court_type function"""

    def test_correct_type(self, court_list_types):
        """Tests that a list of courts with matching 'types' are returned"""
        result = find_correct_court_type(court_list_types, "test_type")
        assert result == [{
        "name" : "test_name",
        "distance": 5,
        "types": ["test_type", "non-matching"],
        "dx_number" : "test_num"
        }]

    def test_non_matching_type(self, court_list_types):
        """Tests that non matching courts are not returned"""
        result = find_correct_court_type(court_list_types, "blah")
        assert result == []


class TestFindClosestCourt:
    """Tests for the get_min_distance_of_court function"""
    
    def test_returns_dict(self, court_list_types):
        """Tests that a dictionary is returned from a list input"""
        result = get_min_distance_of_court(court_list_types)

        assert isinstance(court_list_types, list)
        assert isinstance(result, dict)
    
    def test_returns_minimum_dist(self, court_list_types):
        """Tests that the returned dictionary has a smaller distance value"""
        result = get_min_distance_of_court(court_list_types)
        assert court_list_types[0]["distance"] == 5
        assert court_list_types[1]["distance"] == 4
        assert result["distance"] == 4


class TestPersonOutputDict:
    """Tests for the person_output_dict function"""

    def test_output_is_a_dict(self, close_court, person_list):
        """Tests that this function returns a dict"""
        result = person_output_dict(close_court, person_list)

        assert isinstance(result, dict)
    
    def test_correct_keys(self, close_court, person_list):
        """Tests that the correct keys are in the dict"""
        result = person_output_dict(close_court, person_list)

        assert all(key in result for key in [
            "name",
            "desired_court",
            "home_postcode",
            "nearest_court",
            "dx_number",
            "distance"])
    
    def test_missing_keys_input(self, court_missing_key, person_list):
        result = person_output_dict(court_missing_key, person_list)
        assert result == f"{person_list[0]}: invalid court data"


class TestMainRoutine:
    """Tests for the main_routine functions"""

    @patch("test_2.find_courts")
    def test_no_matching_courts_statement(self, mock_courts, person_string):
        """Tests that the correct statement is returned if there are no valid courts"""
        mock_courts.return_value = []
        result = main_routine(person_string)
        assert result == f"{person_string.split(',')[0]}: no courts of the correct type"
    

    @patch("test_2.find_courts")
    def test_full_routine(self, mock_courts, full_test_courts , person_string):
        """Tests main routine runs with valid arguments and returns dict"""
        mock_courts.return_value = full_test_courts
        result = main_routine(person_string)

        assert isinstance(result,dict)