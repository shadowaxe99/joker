```javascript
// src/frontend/user_privacy.js

// DOM Element
const consentCheckbox = document.getElementById('consentCheckbox');

// Function to check user consent
function checkConsent() {
    if (!consentCheckbox.checked) {
        alert('Please confirm that the recipient has given consent to be pranked.');
        return false;
    }
    return true;
}

// Event Listener for consent checkbox
consentCheckbox.addEventListener('change', checkConsent);
```