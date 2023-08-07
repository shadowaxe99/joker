import React from 'react';
import './App.css';
import ScriptEditor from './components/ScriptEditor';
import VoiceSelector from './components/VoiceSelector';
import CallScheduler from './components/CallScheduler';
import CallInitiator from './components/CallInitiator';
import CallRecorder from './components/CallRecorder';

function App() {
  return (
    <div className='App'>
      <header className='App-header'>
        <h1>Welcome to Joker, the GREATEST prank app ever created!</h1>
        <p>Customize your prank call script, select a voice, schedule the call, and even record the call for endless fun!</p>
      </header>
      <main>
        <ScriptEditor />
        <VoiceSelector />
        <CallScheduler />
        <CallInitiator />
        <CallRecorder />
      </main>
    </div>
  );
}

export default App;