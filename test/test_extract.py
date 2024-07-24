import unittest
import io
import main
import sys
from unittest.mock import Mock, patch

## Import all the necessary libraries

class TestExtract(unittest.TestCase):
# Define a test class that inherits from unittest.TestCase

    @patch('pypdf.PdfReader')
    def test_Extraction(me, check):
        """Is Assignment 0 verfied for extracting text properly and independently"""
        # Setting up mocked PDFReader object and its return values for text extraction
        IncidentData = b'Tablular Information' 
        exp = "\nData from A\nData from B"

        Dummy1 = unittest.mock.MagicMock()
        Dummy1.extract_text.return_value = "Data from A"
        Dummy2 = unittest.mock.MagicMock()
        Dummy2.extract_text.return_value = "Data from B"

        check.return_value.pages = [Dummy1, Dummy2]
        
        # Calling ExtractData and comparing the output with expected text
        og = assignment2.ExractData(IncidentData)
        me.assertEqual(og, exp)
    
        
if __name__ == '__main__':
    unittest.main()
