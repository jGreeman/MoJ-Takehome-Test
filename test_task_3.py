import pytest
from datetime import datetime

from test_3 import sum_current_time, are_times_valid, get_current_time


class TestSumTime:
    """Tests for the sum_current_time function"""

    def test_non_string_input(self):
        """Tests that non-string inputs returns None"""
        assert sum_current_time(15) is None
    
    def test_wrong_time_format(self):
        """Tests that invalid time format returns None"""
        assert sum_current_time("16:12") is None
    
    def test_correct_format(self):
        """Tests that valid time format returns correct sum"""
        assert sum_current_time("13:11:02") == 26
    
    def test_invalid_time(self):
        """Tests that invalid time returns None"""
        assert sum_current_time("25:24:15") is None
    
    def test_negative_time(self):
        """Tests that negative time returns None"""
        assert sum_current_time("-01:14:12") is None


class TestAreTimesValid:
    """Tests for the are_times_valid function"""

    def test_valid_time(self):
        """Tests valid time returns True"""
        assert are_times_valid([12, 13, 55]) is True

    def test_invalid_hour(self):
        """Tests valid time returns True"""
        assert are_times_valid([25, 13, 55]) is False
    
    def test_invalid_minute(self):
        """Tests valid time returns True"""
        assert are_times_valid([12, 77, 55]) is False

    def test_invalid_minute(self):
        """Tests valid time returns True"""
        assert are_times_valid([12, 13, 99]) is False


class TestCurrentTime:
    """Tests for the get_current_time function"""

    def test_returns_string(self):
        assert isinstance(get_current_time(), str)

