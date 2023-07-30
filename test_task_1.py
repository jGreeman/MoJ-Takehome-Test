"""Testing Task_1 functions"""
import pytest
from test_1 import is_log_line, get_dict
from conftest import bad_error_code, invalid_time, missing_message, missing_time, valid_line

class TestValidLine:

    def test_line_not_str(self):
        """Tests that non-string input of is_log_line returns None"""
        assert is_log_line(1) is None

    def test_line_invalid_error(self, bad_error_code):
        """Checks that an invalid error code line returns None"""
        assert is_log_line(bad_error_code) is None

    def test_time_incorrect_format(self, invalid_time):
        """Checks that an invalid time returns None"""
        assert is_log_line(invalid_time) is None

    def test_line_missing_time(self, missing_time):
        """Checks that a line without time returns None"""
        assert is_log_line(missing_time) is None

    def test_line_missing_message(self, missing_message):
        """Checks that a line without time returns None"""
        assert is_log_line(missing_message) is None

    def test_valid_line(self, valid_line):
        """Checks a valid line returns True"""
        assert is_log_line(valid_line) is True

class TestMakeDict:

    def test_makes_dict(self, valid_line):
        result = get_dict(valid_line)
        assert isinstance(result, dict)
        assert all(key in result for key in ["timestamp", "log_level", "message"])
    
    def test_make_dict(self, missing_time):
        assert get_dict(missing_time) is None