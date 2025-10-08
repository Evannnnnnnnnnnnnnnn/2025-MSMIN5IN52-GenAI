const form = document.getElementById('travel-form');
const itineraryDiv = document.getElementById('itinerary');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const destination = document.getElementById('destination').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const budget = document.getElementById('budget').value;

    itineraryDiv.innerHTML = `<p>Planning your trip to ${destination} from ${startDate} to ${endDate} with a budget of ${budget}...</p>`;

    fetch('http://127.0.0.1:5000/plan-trip', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            destination,
            start_date: startDate,
            end_date: endDate,
            budget
        })
    })
    .then(response => response.json())
    .then(data => {
        itineraryDiv.innerHTML = '<h2>Your Itinerary</h2>';
        data.forEach(day_plan => {
            itineraryDiv.innerHTML += `<h3>Day ${day_plan.day}</h3>`;
            day_plan.activities.forEach(activity => {
                if (typeof activity === 'string') {
                    itineraryDiv.innerHTML += `<p>${activity}</p>`;
                } else {
                    itineraryDiv.innerHTML += `<p>${activity.name} (${activity.type})</p>`;
                }
            });

            if (day_plan.weather) {
                if (day_plan.weather.error) {
                    itineraryDiv.innerHTML += `<p>Weather: ${day_plan.weather.error}</p>`;
                } else {
                    itineraryDiv.innerHTML += `<p>Weather: ${day_plan.weather.weather[0].description}</p>`;
                }
            }
        });
    })
    .catch(error => {
        itineraryDiv.innerHTML = `<p>An error occurred: ${error.message}</p>`;
    });
});
