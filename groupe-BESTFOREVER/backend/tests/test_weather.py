
import unittest
from unittest.mock import patch, Mock
import requests
from src.tools.weather import get_weather

class TestWeather(unittest.TestCase):

    @patch.dict('os.environ', {'OPENWEATHER_API_KEY': 'test_key'})
    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        """Test get_weather with a successful API call."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'weather': [{'description': 'clear sky'}],
            'main': {'temp': 25}
        }
        mock_get.return_value = mock_response

        weather_data = get_weather('Paris')

        self.assertEqual(weather_data['main']['temp'], 25)
        self.assertEqual(weather_data['weather'][0]['description'], 'clear sky')

    @patch.dict('os.environ', {'OPENWEATHER_API_KEY': 'test_key'})
    @patch('requests.get')
    def test_get_weather_failure(self, mock_get):
        """Test get_weather with a failed API call."""
        mock_get.side_effect = requests.exceptions.RequestException("API call failed")

        weather_data = get_weather('Paris')

        self.assertIn('error', weather_data)
        self.assertEqual(weather_data['error'], 'An error occurred: API call failed')

    @patch.dict('os.environ', {'OPENWEATHER_API_KEY': ''})
    def test_get_weather_no_api_key(self):
        """Test get_weather when the API key is not set."""
        weather_data = get_weather('Paris')

        self.assertIn('error', weather_data)
        self.assertEqual(weather_data['error'], 'OpenWeather API key not found.')

if __name__ == '__main__':
    unittest.main()

