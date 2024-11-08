import unittest
from dotenv import load_dotenv
import os
import requests

SERVER = "localhost"
API_KEY = os.getenv('SECRET_KEY')
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = requests.get(URL)
available = False
if response.status_code == 200:
    data = response.json()
    print(data)
    available = True
else:
    print(f'Error {response.status_code}: {response.text}')

class AllAssertsTests(unittest.TestCase):
    def test_assert_dict_equal(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"a": 1, "b": 2})
        
    @unittest.skip("Skip this test")
    def test_assert_dict_not_equal(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"a": 1, "b": 3})
        
    @unittest.skipIf(SERVER == "localhost", "Skip this test if SERVER is localhost")    
    def test_assert_list_equal(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])
    
    @unittest.expectedFailure    
    def test_expected_failure(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"a": 1, "b": 3})
        
    @unittest.skipUnless(available, "La API no está disponible para pruebas")
    def test_api_response(self):
        self.assertTrue(available, "La API debería estar disponible")
        if available:
            print("La API está disponible.")