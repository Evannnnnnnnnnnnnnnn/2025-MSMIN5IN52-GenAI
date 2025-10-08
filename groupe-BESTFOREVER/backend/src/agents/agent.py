
from src.tools import get_weather, find_flights, find_hotels, find_activities

class TravelAgent:
    def __init__(self, destination, start_date, end_date, budget):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.itinerary = []

    def plan_trip(self):
        """
        Plans a trip by calling the available tools.
        """
        # 1. Get weather information
        weather_data = get_weather(self.destination)

        # 2. Find flights
        flights_data = find_flights(origin="Paris", destination=self.destination, departure_date=self.start_date, return_date=self.end_date)

        # 3. Find hotels
        hotels_data = find_hotels(city=self.destination, checkin_date=self.start_date, checkout_date=self.end_date)

        # 4. Find activities
        activities_data = find_activities(city=self.destination)

        # 5. Generate itinerary
        self.itinerary = [
            {
                "day": 1,
                "activities": [f"Arrive in {self.destination}"],
                "weather": weather_data,
                "flights": flights_data,
                "hotels": hotels_data
            },
            {
                "day": 2,
                "activities": activities_data.get('activities', [])
            }
        ]

        return self.itinerary

