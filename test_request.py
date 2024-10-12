import requests

# Define the URL to which the POST request will be sent
url = 'http://127.0.0.1:8000/check_feasible_items/'  # Replace with the actual URL

# Define multiple payloads for different test cases
payloads = [
    {
        # Test case 1: Valid items with no modifications
        "Burger": {},    # Standard Burger
        "Fries": {}      # Standard Fries
    },
    {
        # Test case 2: Valid items with extra ingredients
        "Burger": {"Cheese": 2, "Tomato": "-7-"},     # Extra cheese on the burger
        "Fries": {}                  # Standard Fries
    },
    {
        # Test case 3: Valid items with missing ingredients
        "BLT Sandwich": {"Lettuce": 0, "Tomato": 1},  # No lettuce
        "Bacon Cheeseburger": {"Bacon": 0}            # No bacon
    },
    {
        # Test case 4: Non-existent items
        "Pizza": {},    # Item not on the menu
        "Vegan Burger": {}  # Non-existent item
    },
    {
        # Test case 5: Mixed valid and invalid items
        "Burger": {"Cheese": 1},      # Valid item with extra cheese
        "Pizza": {},                  # Non-existent item
        "Fries": {},                  # Valid item
        "Vegan Burger": {}            # Non-existent item
    },
    {
        # Test case 6: Valid item with an unusually large quantity of ingredients
        "Burger": {"Cheese": 10, "Lettuce": 5},  # Extra cheese and lettuce
        "Hot Dog": {"Ketchup": 3}                # Extra ketchup
    },
    {
        # Test case 7: Valid item with less than usual ingredients
        "Bacon Cheeseburger": {"Cheese": 0, "Bacon": 1},  # No cheese, single bacon
        "Fries": {}                                      # Standard Fries
    },
    {
        # Test case 8: Completely invalid items
        "Tacos": {},   # Non-existent item
        "Pasta": {}    # Non-existent item
    }
]

# Function to send POST requests with different payloads and handle responses
def test_payloads(payloads):
    for i, payload in enumerate(payloads, 1):
        print(f"Testing payload {i}...")
        try:
            response = requests.post(url, json={'items': payload})

            # Check if the request was successful (HTTP status code 200 OK)
            if response.status_code == 200:
                # Print the response (usually JSON data)
                print(f"Success (Payload {i}):", response.json())
            else:
                # Print the error message if the request failed
                print(f"Error (Payload {i}):", response.status_code, response.text)

        except requests.exceptions.RequestException as e:
            # Handle any exceptions that may occur during the request
            print(f"An error occurred with payload {i}: {e}")

# Run the tests
test_payloads(payloads)
