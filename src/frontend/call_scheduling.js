```javascript
import axios from 'axios';

// DOM Elements
const scheduleCallForm = document.getElementById('scheduleCall');

// Event Listener for Call Scheduling Form Submission
scheduleCallForm.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get user input
    const date = event.target.elements.date.value;
    const time = event.target.elements.time.value;

    // Schedule the prank call
    scheduleCall(date, time);
});

// Function to Schedule Prank Call
function scheduleCall(date, time) {
    // Prepare data
    const data = {
        date: date,
        time: time
    };

    // Send a POST request to the server
    axios.post('/api/scheduleCall', data)
        .then(response => {
            if (response.data.success) {
                alert('Prank call scheduled successfully!');
            } else {
                alert('Failed to schedule the prank call. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while scheduling the prank call.');
        });
}
```