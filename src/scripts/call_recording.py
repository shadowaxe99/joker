```python
import os
from twilio.twiml.voice_response import Record, VoiceResponse

# Shared variables
callRecordings = {}

def recordCall(call_id, duration=60):
    """
    Function to record the prank call.
    """
    response = VoiceResponse()
    response.say("Recording will start now.")
    response.record(maxLength=duration, action='/handle-recording')
    return str(response)

def handleRecording(request):
    """
    Function to handle the recording after the call ends.
    """
    recording_url = request.values.get('RecordingUrl', None)
    call_id = request.values.get('CallSid', None)

    if recording_url:
        callRecordings[call_id] = recording_url
        return "Recording saved successfully."
    else:
        return "No recording found."

def getRecording(call_id):
    """
    Function to retrieve the recording of a specific call.
    """
    if call_id in callRecordings:
        return callRecordings[call_id]
    else:
        return "No recording found for this call."

def downloadRecording(call_id):
    """
    Function to download the recording of a specific call.
    """
    recording_url = getRecording(call_id)
    if recording_url.startswith("http"):
        os.system(f"wget -O {call_id}.mp3 {recording_url}")
        return f"Recording {call_id}.mp3 downloaded successfully."
    else:
        return recording_url
```