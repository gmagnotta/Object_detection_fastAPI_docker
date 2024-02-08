import requests

# API endpoint URL
api_endpoint = "http://localhost:8000/detect/"

# Test images folder
test_images_folder = "test_images/"

# Dictionary to store test status
test_status = {}

# Function to send a POST request to the detection API and log the test status
def test_object_detection(image_path, label=None, test_number=0):
    # Prepare request payload
    files = {"image": open(image_path, "rb")}
    api_endpoint_with_label = f"{api_endpoint}?label={label}" if label else api_endpoint
      
    # Send POST request
    response = requests.post(api_endpoint_with_label, files=files)
    
    # Check response status
    if response.status_code == 200:
        # Successful response
        result = response.json()
        print("Test Image:", image_path)
        print("Detection Results:", result)
        
        # If no label specified
        if label is None:
            test_status[f"Test {test_number}"] = "Success"
            print("Success!")
        # If objects are detected with the specified label
        elif result["count"] > 0 and result["objects"][0]["label"] == label:
            test_status[f"Test {test_number}"] = "Success"
            print("Success!")
        else:
            # If the test fails
            test_status[f"Test {test_number}"] = "Failure"
            print("Failure!!!")
    else:
        # If the API request fails
        print("API request failed:", response.text)

# Test scenario 1: Detect objects without specifying a label
test_object_detection(test_images_folder + "test_image1_bus_people.jpg", label=None, test_number=1)
    
# Test scenario 2: Detect only "bird" objects
test_object_detection(test_images_folder + "test_image2_bird.jpg", label="bird", test_number=2)

# Test scenario 3: Detect only "dog" objects
test_object_detection(test_images_folder + "test_image3_dog.jpg", label="dog", test_number=3)

# Print test status
print("Test Status:", test_status)


