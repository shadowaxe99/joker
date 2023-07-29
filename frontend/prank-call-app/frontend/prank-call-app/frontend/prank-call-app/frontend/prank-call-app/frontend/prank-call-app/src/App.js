import React, { useState } from 'react';

const App = () => {
  const [name, setName] = useState('');
  const [prankMessage, setPrankMessage] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name && prankMessage) {
      // Logic to send prank message
    // Code to generate voice message
import Voice from './Voice';
    const generateVoiceMessage = () => {
      // Code to generate voice message
import Voice from './Voice';
    }
      setSubmitted(true);
      setError('');
    } else {
      setError('Please enter both name and prank message.');
    }
  };

  const handleReset = () => {
    setName('');
    setPrankMessage('');
    setSubmitted(false);
    setError('');
  };

  return (
    <div>
      <h1>Your Your App</h1>
      {error && <div className="error-notification">{error}</div>}
      {!submitted ? (
        <form onSubmit={handleSubmit}>
          <label>
            Name:
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
          </label>
          <br />
          <label>
            Prank Message:
            <textarea value={prankMessage} onChange={(e) => setPrankMessage(e.target.value)} />
          </label>
          <br />
          <button type="submit">Submit</button>
        </form>
      ) : (
        <div>
          <h2>Prank Message:</h2>
          <LowLatency />
          <Voice />
          <Voice />
          <p>{prankMessage}</p>
          <p>Sent by: {name}</p>
          <button onClick={handleReset}>Reset</button>
        </div>
      )}
    </div>
  );
};

export default App;
