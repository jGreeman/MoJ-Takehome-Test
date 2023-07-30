# MOJ Take Home Test

## Intro

This repository contains the solutions to three tests as part of the MoJ take-home test.

Test 1 checks whether a log line is in a valid format, and then creates a dictionary for each line in the log.
Test 2 finds the nearest correct court type for each person in the file _people.csv_, containing their name, postcode and court type.
this is done by connecting to an api and selecting the relevant data.
Test 3 sums up each number of the current time in the format _HH:MM:SS_.

### Set-up

Install requirements with the following command:

    pip3 install -r requirements

## Running the code

The code for each task can be run by using the command:

    python3 test_[x].py

## Testing

Each task also contains unit testing in files titled: _test_task\_[x].py_ that can be run using the following command:

    pytest test_task_[x].py
