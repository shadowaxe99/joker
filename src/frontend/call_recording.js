```javascript
import axios from 'axios';

// DOM Elements
const recordCall = document.getElementById('recordCall');

// Event Listener for Record Call Checkbox
recordCall.addEventListener('change', (event) => {
    if (event.target.checked) {
        enableCallRecording();
    } else {
        disableCallRecording();
    }
});

// Function to Enable Call Recording
function enableCallRecording() {
    axios.post('/api/enableCallRecording')
        .then(response => {
            if (response.data.success) {
                console.log('Call recording enabled');
            } else {
                console.error('Failed to enable call recording');
            }
        })
        .catch(error => {
            console.error('Error enabling call recording:', error);
        });
}

// Function to Disable Call Recording
function disableCallRecording() {
    axios.post('/api/disableCallRecording')
        .then(response => {
            if (response.data.success) {
                console.log('Call recording disabled');
            } else {
                console.error('Failed to disable call recording');
            }
        })
        .catch(error => {
            console.error('Error disabling call recording:', error);
        });
}
```