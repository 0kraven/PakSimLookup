import argparse
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable 

# Function to display the GitHub profile and banner
def show_banner():
    banner = """

    ==========================================================================    
   | Use this tool to fetch details using either:                             |
   | --number <number> (must start with 92) or --cnic <cnic> (without dashes) |
   |++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
   | Example Usage:                                                           |
   | python3 paksimlookup.py --number 923001234567                            |
   | python3 paksimlookup.py --cnic 1234512345671                             |
   |__________________________________________________________________________|
                                         | GitHub: 0kraven | justanormalguy   |
                                         |____________________________________|     
    """

    print(banner)

# Function to validate the phone number (should start with 92)
def validate_phone_number(number):
    if number.startswith("92") and len(number) == 12 and number.isdigit():
        return True
    else:
        print("Error: The phone number must start with 92 and be 12 digits long.")
        return False

# Function to validate the CNIC (should be without dashes)
def validate_cnic(cnic):
    if len(cnic) == 13 and cnic.isdigit():
        return True
    else:
        print("Error: CNIC should be 13 digits long and without dashes.")
        return False

# Function to send the request and fetch details
def fetch_details(arg):
    # URL to post the request to
    url = 'https://pakistandatabase.com/databases/sim.php'

    # Parameters to send with the POST request
    param = {"search_query": arg}

    try:
        # Send POST request
        response = requests.post(url, param)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

        # Parse the response content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing the relevant data
        table = soup.find('table', class_='api-response')

        # If the table is found, proceed with extraction
        if table:
            # Extract column headers (Mobile, Name, CNIC, Address)
            headers = [header.text.strip() for header in table.find_all('th')]

            # Create a PrettyTable object
            pretty_table = PrettyTable(headers)

            # Extract rows of data and add them to the PrettyTable
            for row in table.find_all('tr')[1:]:  # Skip the header row
                cols = row.find_all('td')
                if cols:
                    row_data = [col.text.strip() for col in cols]
                    # Check if the row has the correct number of values
                    if len(row_data) == len(headers):
                        pretty_table.add_row(row_data)
                    else:
                        print("No Record Found.")
            # Return the formatted table
            return pretty_table
        else:
            print("No table found in the response.")
            return None
    except requests.exceptions.RequestException as e:
        print("Connection error occurred.")
        return None

# Function to handle argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Pakistan Database Lookup Tool')
    parser.add_argument('--number', type=str, help='Phone number to look up details')
    parser.add_argument('--cnic', type=str, help='CNIC number to look up details')

    args = parser.parse_args()

    # Ensure that either --number or --cnic is provided
    if not args.number and not args.cnic:
        show_banner()  # Show the help banner when no argument is passed
        return None  # Return None if no arguments are provided

    return args

# Main function to drive the script
def main():
    # Parse the arguments
    args = parse_arguments()

    # If no arguments are provided, return early
    if not args:
        return

    # Fetch details based on input
    if args.number:
        identifier_type = 'number'
        identifier_value = args.number
        # Validate the phone number
        if not validate_phone_number(identifier_value):
            return
    elif args.cnic:
        identifier_type = 'cnic'
        identifier_value = args.cnic
        # Validate the CNIC
        if not validate_cnic(identifier_value):
            return

    banner = R"""
=======================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
+         ____________                                +
+        < Extractor! >                               +
+         ------------                                +
+                \   ^__^                             +
+                 \  (oo)\_______                     +
+                    (__)\       )\/\                 +
+                        ||----w |                    +
+                        ||     ||                    +
+                                                     +
+        A simple tool to extract CNIC and number.    +
+       [--------> Unmask the digits 0_0 <--------]   +	
+           GitHub: 0kraven | justanormalguy          +
+          <================================>         +
+                                                     +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
=======================================================
    """
    print(banner)

    # Fetch the details from the website
    details = fetch_details(identifier_value)

    # Output the results
    if details:
        print(details)
    else:
        print(f"Failed to fetch data for {identifier_type}: {identifier_value}. Please try again or ensure you're connected to a VPN.")

# Entry point of the script
if __name__ == '__main__':
    main()
