import sys # The sys module provides information about constants, functions and methods of the Python interpreter
import requests # Requests is a Python module that you can use to send all kinds of HTTP requests
import hashlib  # The hashlib module implements a common interface to many different secure hash and message digest algorithms

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char  # Password123 is the password to be checked against the API
    response = requests.get(url)  # Sends a GET request to the API
    print(response)  # Prints the response code (200 = OK)  (400 = Bad Request) (404 = Not Found) (500 = Internal Server Error)
    if response.status_code!=200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again")
    return response
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()  # Hashes the password to SHA1
    first5_char, tail = sha1password[:5], sha1password[5:]  # Splits the hashed password into two parts
    response = request_api_data(first5_char)  # Sends the first 5 characters of the hashed password to the API
    return get_password_leaks_count(response, tail)  # Returns the number of times the password has been leaked

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())  # Splits the response into two parts (hash and count)
    for h, count in hashes:  # For each hash and count in the response
        if h == hash_to_check:  # If the hash matches the hash of the password
            return count  # Return the count
    return 0  # If the password has not been leaked, return 0

def main(args):
    for password in args:  # For each password in the arguments
        count = pwned_api_check(password)  # Check the password against the API
        if count:  # If the password has been leaked
            password_stars = "*" * len(password)  # Creates a string of * the same length as the password
            print(f"{password_stars} was found {count} times... you should probably change your password!")
        else:  # If the password has not been leaked
            print(f"{password_stars} was NOT found. Carry on!")
    return "Done!"

if __name__ == "__main__":
   sys.exit(main(sys.argv[1:]))  # Runs the main function with the arguments passed in