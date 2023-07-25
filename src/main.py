```python
import sys
from src.voice_synthesis import generateVoice
from src.prank_call_customization import customizeScript
from src.call_scheduling import scheduleCall
from src.call_recording import recordCall
from src.user_privacy import checkConsent
from src.nlp_processing import processInput
from src.call_handling import initiateCall
from src.backend.user_requests import handleUserRequest
from src.backend.prank_call_scripts import storePrankCallScript
from src.backend.user_preferences import storeUserPreferences
from src.backend.scheduled_prank_calls import storeScheduledCall
from src.backend.call_recordings import storeCallRecording

def main():
    # User preferences
    userPreferences = {}

    # Scheduled prank calls
    scheduledCalls = []

    # Call recordings
    callRecordings = []

    # Handle user requests
    userRequest = handleUserRequest()

    # Check user consent
    if not checkConsent(userRequest):
        print("Consent not provided. Exiting...")
        sys.exit()

    # Customize script
    customizedScript = customizeScript(userRequest, userPreferences)

    # Generate voice
    voice = generateVoice(userPreferences)

    # Schedule call
    scheduledCall = scheduleCall(userRequest)

    # Store user preferences
    storeUserPreferences(userPreferences)

    # Store prank call script
    storePrankCallScript(customizedScript)

    # Store scheduled call
    storeScheduledCall(scheduledCall)

    # Initiate call
    callResult = initiateCall(voice, customizedScript, scheduledCall)

    # Record call
    if userPreferences.get('recordCall'):
        callRecording = recordCall(callResult)
        storeCallRecording(callRecording)

if __name__ == "__main__":
    main()
```