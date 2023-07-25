```javascript
import React, { useState } from 'react';
import PrankCallCustomization from './prank_call_customization.js';
import CallScheduling from './call_scheduling.js';
import CallRecording from './call_recording.js';
import UserPrivacy from './user_privacy.js';

const UserInterface = () => {
    const [userPreferences, setUserPreferences] = useState({});
    const [scheduledCalls, setScheduledCalls] = useState([]);
    const [callRecordings, setCallRecordings] = useState([]);

    const handleVoiceSelection = (selectedVoice) => {
        setUserPreferences({...userPreferences, selectedVoice});
    };

    const handleScriptInput = (script) => {
        setUserPreferences({...userPreferences, script});
    };

    const handleCallScheduling = (schedule) => {
        setScheduledCalls([...scheduledCalls, schedule]);
    };

    const handleCallRecording = (recording) => {
        setCallRecordings([...callRecordings, recording]);
    };

    const handleConsentCheckbox = (consent) => {
        setUserPreferences({...userPreferences, consent});
    };

    return (
        <div>
            <h1>AI-Powered Prank Dialer</h1>
            <PrankCallCustomization 
                onVoiceSelection={handleVoiceSelection} 
                onScriptInput={handleScriptInput} 
            />
            <CallScheduling onCallScheduling={handleCallScheduling} />
            <CallRecording onCallRecording={handleCallRecording} />
            <UserPrivacy onConsentCheckbox={handleConsentCheckbox} />
        </div>
    );
};

export default UserInterface;
```