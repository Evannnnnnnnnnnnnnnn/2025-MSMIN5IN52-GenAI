
import unittest
from src.tools.flights import find_flights

class TestFlights(unittest.TestCase):

    def test_find_flights_mocked(self):
        """Test find_flights with mocked data."""
        flights_data = find_flights('Paris', 'Tokyo', '2025-10-20', '2025-10-30')

        self.assertIn('flights', flights_data)
        self.assertEqual(len(flights_data['flights']), 1)
        self.assertEqual(flights_data['flights'][0]['airline'], 'Mock Airline')

if __name__ == '__main__':
    unittest.main()

