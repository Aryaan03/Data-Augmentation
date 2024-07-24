import pytest
from unittest.mock import Mock, patch
from main import RetrieveIncidents, ExractData, DataBase, Coord, TownSide, Weather, Output, Insert


# # Mocking Database function for testing
# @patch('a2copy.sqlite3.connect')
# def test_DataBase(mock_connect):
#     mock_cursor = mock_connect.return_value.cursor.return_value
#     Norman = "test.db"
#     Tab = "test_table"
#     Info = [("01/01/2023 12:00", "Location", "Nature", "Incident_ori")]
#     DataBase(Norman, Tab, Info)
#     mock_cursor.execute.assert_called_once()

# Mocking Coord function for testing
@patch('main.requests.get')
def test_Coord_valid_address(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "features": [{"geometry": {"coordinates": [40.7128, -74.006]} }]
    }
    mock_get.return_value = mock_response
    lat, lon = Coord("New York")
    assert lat == -74.006
    assert lon == 40.7128


# Test TownSide function
def test_TownSide():
    side = TownSide("Location")
    assert side in ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE', 'E']

# Mocking Weather function for testing
# @patch('main.openmeteo_requests.Client')
# def test_Weather(mock_client):
#     mock_client.return_value.weather_api.return_value = [
#     Mock(Hourly=Mock(Time=lambda: 1640995200, TimeEnd=lambda: 1640998800, Interval=lambda: 3600)),
#     Mock(Variables=lambda x: Mock(ValuesAsNumpy=lambda: [100, 0, 200])) # Example weather data
# ]
#     weather_code = Weather("Location", "01/01/2023 12:00")
#     assert weather_code == 200

# Mocking Output function for testing
@patch('main.sqlite3.connect')
def test_Output(mock_connect):
    mock_cursor = mock_connect.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [(1, 12, 200, 1, 'E', 1, 'Nature', 0)]
    Output("test.db", "test_table")
    assert mock_cursor.execute.called

# Test Insert function
def test_Insert():
    Latest = []
    Information = [("D", "01/01/2023 12:00", "Location", "Nature", "Incident_ori")]
    Latest = Insert(Information, Latest)
    assert len(Latest) == 1
