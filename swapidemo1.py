#!/usr/bin/env python3
"""Start Wars API HTTP response parsing"""

# requests is used to send HTTP requests (get it?)
import requests

URL = "https://swapi.dev/api/people/1"

def main():
    """Sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp = requests.get(URL)

    # what kind of pythin object is "resp"?
    print("This object class is:", type(resp), "\n")

    # what can we do with it?
    print("Methods/Attributes include:", dir(resp))

if __name__ == "__main__":
    main()