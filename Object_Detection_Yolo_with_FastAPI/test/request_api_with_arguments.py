import argparse
import requests
import sys

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Send image detection request to API")
parser.add_argument("-f", "--file", type=str, help="Image file name")
parser.add_argument("-l", "--label", type=str, help="Label parameter")
args = parser.parse_args()

# Check if image file is provided
if args.file:
    # API endpoint URL
    api_endpoint = "http://localhost:8000/detect/"

    # Image file name
    image_filename = args.file

    # Label parameter
    label = args.label if args.label else ""

    # Upload the image
    files = {"image": open(image_filename, "rb")}

    # Concatenate API endpoint URL with label parameter if provided
    api_endpoint_with_label = f"{api_endpoint}?label={label}" if label else api_endpoint

    # Send a POST request
    response = requests.post(api_endpoint_with_label, files=files)

    # Check the response
    if response.status_code == 200:
        # Successful response
        result = response.json()
        print(result)
    else:
        # Error response
        print("API request failed:", response.text)
else:
    print("Error: Image file not provided.")
    sys.exit(1)
