import requests
import json

def test_successful_request_returns_200():
    url = 'https://petstore.swagger.io/'     
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_successful_request_returns_valid_json():
    url = 'https://petstore.swagger.io/'  
    response = requests.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    try:
        json_data = response.json()
        assert isinstance(json_data, dict), "Response data is not a valid JSON object"
        
    except json.JSONDecodeError:
        assert False, "Response data is not a valid JSON format"


def test_invalid_request_returns_correct_http_status_code():
    url = 'https://petstore.swagger.io/'  
    invalid_params = {'param1': 'value1', 'param2': 'value2'}  

    response = requests.get(url, params=invalid_params)

    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
