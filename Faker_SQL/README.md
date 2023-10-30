# Project: Company Data Generator

This project consists of a Python script that generates fake company data and constructs SQL commands to insert this data into a database. It uses the `faker` library to create realistic names, addresses, emails, and other details, and writes the SQL commands to a file named `create_companies.sql`.

## Features

- Generates 100,000 fake company profiles with the following details:
  - First name, Last name
  - Company name (in the format "Firstname Lastname GmbH")
  - Secure password
  - Randomly assigned main category ID
  - Unique email addresses with appended UUIDs
  - Phone numbers with appended UUIDs
  - Addresses including street, building number, postcode, city, and state
  - GISA number (unique identifier, represented by UUID)
  - Country code set to "AT" for Austria
- Writes generated SQL insert commands to `create_companies.sql`.
- Ensures all email and phone number entries are unique by appending a UUID.
- Provides a sample printout of the first 10 SQL commands for verification.

## Requirements

- Python 3
- `faker` library: Can be installed via pip with `pip install Faker`.

## Usage

To use the script, follow these steps:

1. Ensure that Python 3 and the `faker` library are installed on your machine.
2. Run the script using a Python interpreter.
3. The script will generate the data and write the SQL commands to `create_companies.sql`.
4. You can then use this SQL file to insert the data into your database.

## Output

The script outputs a file named `create_companies.sql` with SQL insert commands for each generated company profile.
