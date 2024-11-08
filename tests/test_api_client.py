import unittest, requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    @patch("src.api_client.requests.get")
    def test_get_location_by_ip(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'city': 'Mountain View', 
            'region': 'California', 
            'country_name': 'United States', 
        }
        location = get_location("8.8.8.8")
        self.assertEqual(location.get("city"), "Mountain View")
        self.assertEqual(location.get("region"), "California")
        self.assertEqual(location.get("country"), "United States")
        mock_get.assert_called_once_with("https://ipapi.co/8.8.8.8/json/")
        
    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [requests.exceptions.RequestException("Service Unavailable"),
                                unittest.mock.Mock(status_code=200, json=lambda: {
                                    'city': 'Mountain View', 
                                    'region': 'California', 
                                    'country_name': 'United States', 
                                })]
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")
        
        location = get_location("8.8.8.8")
        self.assertEqual(location.get("city"), "Mountain View")
        self.assertEqual(location.get("region"), "California")
        self.assertEqual(location.get("country"), "United States")
        