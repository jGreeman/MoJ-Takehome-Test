"""
This script takes a time string input, and returns the sum of each number in the time
"""
from datetime import datetime

def are_times_valid(time_list: list[int])->bool:
    """Checks that the numbers in the time are valid"""
    if time_list[0] >= 24 or time_list[0] < 0:
        return False
    if time_list[1] >= 60 or time_list[1] < 0:
        return False
    if time_list[2] >= 60 or time_list[2] < 0:
        return False
    return True

def get_current_time():
    """Using datetime library returns current time"""
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def sum_current_time(time_str: str) -> int | None:
    """
    Expects data in the format HH:MM:SS,
    takes a string representing time, and returns the sum of numbers.
    """
    try:
        list_of_nums = [int(number) for number in time_str.split(":")]
        if len(list_of_nums) != 3:
            raise ValueError("String must be in format HH:MM:SS")
        if not are_times_valid(list_of_nums):
            raise ValueError("Times must be in valid 24hr time format")
        return sum(list_of_nums)

    except ValueError as err:
        print(err.args[0])
        return None

    except AttributeError as err:
        print(err.args[0])
        return None


if __name__ == "__main__":
    print(sum_current_time(get_current_time()))
