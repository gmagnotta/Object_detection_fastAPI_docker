import requests

# API endpoint URL
api_endpoint = "http://localhost:8000/detect/"

# Image file name
image_filename = "bus.jpg"

# Label parameter
label = ""

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
