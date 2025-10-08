
import unittest
from src.tools.activities import find_activities

class TestActivities(unittest.TestCase):

    def test_find_activities_mocked(self):
        """Test find_activities with mocked data."""
        activities_data = find_activities('Paris')

        self.assertIn('activities', activities_data)
        self.assertEqual(len(activities_data['activities']), 2)
        self.assertEqual(activities_data['activities'][0]['name'], 'Mock Museum')

if __name__ == '__main__':
    unittest.main()

