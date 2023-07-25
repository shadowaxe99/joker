```javascript
import React, { useState } from 'react';
import axios from 'axios';

const PrankCallCustomization = () => {
  const [script, setScript] = useState('');
  const [voice, setVoice] = useState('');

  const handleScriptChange = (event) => {
    setScript(event.target.value);
  };

  const handleVoiceChange = (event) => {
    setVoice(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const prankCallData = {
      script: script,
      voice: voice,
    };

    axios.post('/api/prankCallCustomization', prankCallData)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Script:
          <textarea id="scriptInput" value={script} onChange={handleScriptChange} />
        </label>
        <label>
          Voice:
          <select id="voiceSelection" value={voice} onChange={handleVoiceChange}>
            <option value="celebrity">Celebrity</option>
            <option value="cartoon">Cartoon Character</option>
            <option value="fictional">Fictional Personality</option>
          </select>
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default PrankCallCustomization;
```