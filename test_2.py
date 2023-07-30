"""Script to find the nearest court of the correct type for each person
listed in a CSV file, with their preferred court type"""
import requests

CSV_FILE = "people.csv"
NAME = "name"
DISTANCE = "distance"
TYPES = "types"
DX_NUMBER = "dx_number"

def get_csv_data(filename:str)->list[str]:
    """Opens a CSV file and returns a list of strings of each row"""
    with open(filename, "r") as file:
        data = list(file)
    return data


def find_courts(postcode:str)->list[dict]:
    """Given an input string, connects to API and returns data for 10 closest courts"""
    data = requests.get(
        f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}",
        timeout=5)
    data.raise_for_status()
    return [{NAME : row[NAME],
                DISTANCE : row[DISTANCE],
                TYPES : row[TYPES],
                DX_NUMBER : row[DX_NUMBER]}
                for row in data.json()]


def find_correct_court_type(courts: list[dict], court_type:str)->list[dict]:
    """Takes list of courts and returns those of the correct type"""
    return [court for court in courts if court_type in court[TYPES]]


def get_min_distance_of_court(correct_courts:list[dict])->dict:
    """Returns the court with the minimum distance from list of courts"""
    return min(correct_courts, key = lambda x:x[DISTANCE])


def person_output_dict(closest_court:dict, person:list)->dict:
    """Given the nearest court, and a row of a person from the CSV,
    combines the information and returns as a dictionary
    """
    try:
        return {
            NAME : person[0],
            "desired_court" : person[2].strip("\n"),
            "home_postcode" : person[1],
            "nearest_court" : closest_court[NAME],
            DX_NUMBER     : closest_court[DX_NUMBER],
            DISTANCE      : closest_court[DISTANCE]
        }
    except KeyError as err:
        print(err.args[0])
        return f"{person[0]}: invalid court data"


def main_routine(person:str)->dict | str:
    """Given a row of a person from the CSV, runs all the functions needed to find
    their nearest court of the correct type, and combine info into one dict"""
    postcode = person.split(",")[1]
    court_type = person.split(",")[2].strip()

    try:
        all_courts = find_courts(postcode)
    except requests.HTTPError as err:
        print(err.response)
        return f"{person.split(',')[0]}: unable to connect to API"

    correct_courts = find_correct_court_type(all_courts, court_type)
    if correct_courts == []:
        return f"{person.split(',')[0]}: no courts of the correct type"

    closest_court = get_min_distance_of_court(correct_courts)

    return person_output_dict(closest_court, person.split(","))


if __name__ == "__main__":
    people = get_csv_data(CSV_FILE)
    people.pop(0)
    people_list = [main_routine(person) for person in people]

    for row in people_list:
        print(row)
