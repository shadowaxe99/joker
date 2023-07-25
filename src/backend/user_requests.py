```python
from flask import Flask, request, jsonify
from src.voice_synthesis import generateVoice
from src.prank_call_customization import customizeScript
from src.call_scheduling import scheduleCall
from src.call_recording import recordCall
from src.user_privacy import checkConsent
from src.nlp_processing import processInput
from src.call_handling import initiateCall
from src.backend.database import UserSchema, CallSchema, RecordingSchema

app = Flask(__name__)

@app.route('/user_request', methods=['POST'])
def handleUserRequest():
    user_request = request.get_json()

    # Check if user request is valid
    if not UserSchema.validate(user_request):
        return jsonify({"message": "Invalid user request"}), 400

    # Check if recipient has given consent
    if not checkConsent(user_request['recipient']):
        return jsonify({"message": "Recipient has not given consent"}), 403

    # Process user input
    processed_input = processInput(user_request['input'])

    # Customize prank call script
    customized_script = customizeScript(processed_input)

    # Generate voice for prank call
    voice = generateVoice(user_request['voice'])

    # Schedule prank call
    scheduled_call = scheduleCall(user_request['schedule'])

    # Initiate prank call
    call_status = initiateCall(voice, customized_script, scheduled_call)

    # Record prank call if user has opted for it
    if user_request['record']:
        recording = recordCall(call_status)
        if not RecordingSchema.validate(recording):
            return jsonify({"message": "Error in recording prank call"}), 500

    return jsonify({"message": "Prank call initiated successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```