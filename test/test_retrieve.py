import unittest
import io
import assignment2
import sys
from unittest.mock import Mock, patch

## Import all the necessary libraries

class TestReterieve(unittest.TestCase):
# Define a test class that inherits from unittest.TestCase
   
    # Decorate the test method with patch to mock the 'urllib.request.urlopen' and 'urllib.request.Request' functions
    @patch('urllib.request.urlopen')
    @patch('urllib.request.Request')
    def test_Retrieve(me, ask, mdo):
        mdo.return_value.read.return_value = b'Dummy'
        # Mock the return value of the read function of the urlopen object

        url = 'https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-04_daily_incident_summary.pdf'
        out = assignment2.RetrieveIncidents(url)

        # Verifying if urlopen was called with the provided URL and headers
        ask.assert_called_once_with(url, headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        # Verifying if Request was called with the return value of urlopen
        mdo.assert_called_once_with(ask.return_value)
     
        # Verifying if the output matches the expected 'Dummy' content
        me.assertEqual(out, b'Dummy')
        
if __name__ == '__main__':
    unittest.main()
