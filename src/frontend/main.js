```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import UserInterface from './user_interface.js';
import PrankCallCustomization from './prank_call_customization.js';
import CallScheduling from './call_scheduling.js';
import CallRecording from './call_recording.js';
import UserPrivacy from './user_privacy.js';

class Main extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userPreferences: {},
            scheduledCalls: [],
            callRecordings: []
        };
    }

    handleUserPreferencesUpdate = (preferences) => {
        this.setState({ userPreferences: preferences });
    }

    handleScheduledCallsUpdate = (calls) => {
        this.setState({ scheduledCalls: calls });
    }

    handleCallRecordingsUpdate = (recordings) => {
        this.setState({ callRecordings: recordings });
    }

    render() {
        return (
            <div>
                <UserInterface 
                    userPreferences={this.state.userPreferences} 
                    onUserPreferencesUpdate={this.handleUserPreferencesUpdate}
                />
                <PrankCallCustomization 
                    userPreferences={this.state.userPreferences} 
                    onUserPreferencesUpdate={this.handleUserPreferencesUpdate}
                />
                <CallScheduling 
                    scheduledCalls={this.state.scheduledCalls} 
                    onScheduledCallsUpdate={this.handleScheduledCallsUpdate}
                />
                <CallRecording 
                    callRecordings={this.state.callRecordings} 
                    onCallRecordingsUpdate={this.handleCallRecordingsUpdate}
                />
                <UserPrivacy 
                    userPreferences={this.state.userPreferences} 
                    onUserPreferencesUpdate={this.handleUserPreferencesUpdate}
                />
            </div>
        );
    }
}

ReactDOM.render(<Main />, document.getElementById('root'));
```