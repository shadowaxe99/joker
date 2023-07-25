Shared Dependencies:

1. **Exported Variables:**
   - `userPreferences`: Stores user's preferences like selected voice, script customization, etc.
   - `scheduledCalls`: Stores information about scheduled prank calls.
   - `callRecordings`: Stores information about recorded prank calls.

2. **Data Schemas:**
   - `UserSchema`: Defines the structure for user data.
   - `CallSchema`: Defines the structure for prank call data.
   - `RecordingSchema`: Defines the structure for call recording data.

3. **DOM Element IDs:**
   - `voiceSelection`: Dropdown for selecting the voice for the prank call.
   - `scriptInput`: Text area for customizing the prank call script.
   - `scheduleCall`: Input fields for scheduling the prank call.
   - `recordCall`: Checkbox for deciding whether to record the prank call or not.
   - `consentCheckbox`: Checkbox for confirming the recipient's consent.

4. **Message Names:**
   - `PrankCallInitiated`: Message sent when a prank call is initiated.
   - `PrankCallScheduled`: Message sent when a prank call is scheduled.
   - `PrankCallRecorded`: Message sent when a prank call is recorded.

5. **Function Names:**
   - `generateVoice()`: Function in `voice_synthesis.py` to generate the voice for the prank call.
   - `customizeScript()`: Function in `prank_call_customization.py` to customize the prank call script.
   - `scheduleCall()`: Function in `call_scheduling.py` to schedule the prank call.
   - `recordCall()`: Function in `call_recording.py` to record the prank call.
   - `checkConsent()`: Function in `user_privacy.py` to check the recipient's consent.
   - `processInput()`: Function in `nlp_processing.py` to process user inputs.
   - `initiateCall()`: Function in `call_handling.py` to initiate the prank call.
   - `handleUserRequest()`: Function in `user_requests.py` to handle user requests.
   - `storePrankCallScript()`: Function in `prank_call_scripts.py` to store the prank call script.
   - `storeUserPreferences()`: Function in `user_preferences.py` to store user preferences.
   - `storeScheduledCall()`: Function in `scheduled_prank_calls.py` to store scheduled prank calls.
   - `storeCallRecording()`: Function in `call_recordings.py` to store call recordings.