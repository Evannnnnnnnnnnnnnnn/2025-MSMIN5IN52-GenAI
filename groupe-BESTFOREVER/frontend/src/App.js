import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');
    try {
      const res = await fetch('http://localhost:8000/plan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: query }),
      });
      const data = await res.json();
      setResponse(data.plan);
    } catch (error) {
      console.error('Error fetching plan:', error);
      setResponse('Failed to get a response from the agent.');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Travel Agent Planner</h1>
        <p>Enter your travel details below and let the agent plan your trip!</p>
      </header>
      <main>
        <form onSubmit={handleSubmit}>
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g., I want to go to Paris for 5 days with a budget of 2000 euros."
            rows="5"
            cols="50"
          />
          <br />
          <button type="submit" disabled={loading}>
            {loading ? 'Planning...' : 'Get Plan'}
          </button>
        </form>
        {response && (
          <div className="response">
            <h2>Your Travel Plan:</h2>
            <p>{response}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
