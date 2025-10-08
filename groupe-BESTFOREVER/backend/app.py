
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.agents import TravelAgent

app = Flask(__name__)
CORS(app)

@app.route('/plan-trip', methods=['POST'])
def plan_trip():
    data = request.get_json()

    destination = data.get('destination')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    budget = data.get('budget')

    if not all([destination, start_date, end_date, budget]):
        return jsonify({'error': 'Missing required fields'}), 400

    agent = TravelAgent(destination, start_date, end_date, budget)
    itinerary = agent.plan_trip()

    return jsonify(itinerary)

if __name__ == '__main__':
    app.run(debug=True)

