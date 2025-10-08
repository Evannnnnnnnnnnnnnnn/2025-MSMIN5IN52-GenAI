
import unittest
from src.tools.hotels import find_hotels

class TestHotels(unittest.TestCase):

    def test_find_hotels_mocked(self):
        """Test find_hotels with mocked data."""
        hotels_data = find_hotels('Paris', '2025-10-20', '2025-10-30')

        self.assertIn('hotels', hotels_data)
        self.assertEqual(len(hotels_data['hotels']), 1)
        self.assertEqual(hotels_data['hotels'][0]['name'], 'Mock Hotel')

if __name__ == '__main__':
    unittest.main()

