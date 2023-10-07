# Pwned Password Checker

This script checks if your passwords have been leaked in any known data breaches using the Have I Been Pwned API.

## Features:
1. Securely checks passwords against the Have I Been Pwned API.
2. Uses SHA-1 hashing to ensure privacy.
3. Can check multiple passwords in a single run.

## Requirements:
- Python 3.x
- `requests` module (install via pip: `pip install requests`)

## Usage:

Run the script from the terminal or command line and pass the passwords you want to check as arguments:

python pwned_checker.py password1 password2 ...

makefile


Example:

python pwned_checker.py mypassword123 secretPass

vbnet


The script will then securely check these passwords against the API and inform you if they've been found in any known breaches.

## How it works:

    1. The password is hashed using the SHA-1 algorithm.
    2. The first 5 characters of this hash are sent to the Have I Been Pwned API.
    3. The API returns a list of hashes that match the first 5 characters.
    4. The script checks if the full hash of your password is in this list.
    5. If found, it displays how many times this password has been leaked.

## Security:

The script only sends the first 5 characters of the SHA-1 hash of your password. This ensures that your password is never sent in full and remains private.

## Notes:
- The passwords are represented by asterisks in the output to avoid displaying sensitive information in the terminal.
- Always ensure to use strong, unique passwords for all your accounts.
- Consider using a password manager to keep track of your passwords.