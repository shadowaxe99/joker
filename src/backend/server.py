```python
from flask import Flask, request, jsonify
from database import init_db, db_session
from user_requests import handleUserRequest
from prank_call_scripts import storePrankCallScript
from user_preferences import storeUserPreferences
from scheduled_prank_calls import storeScheduledCall
from call_recordings import storeCallRecording

app = Flask(__name__)
init_db()

@app.route('/api/user-request', methods=['POST'])
def user_request():
    data = request.get_json()
    response = handleUserRequest(data)
    return jsonify(response)

@app.route('/api/store-script', methods=['POST'])
def store_script():
    data = request.get_json()
    storePrankCallScript(data)
    return jsonify({'message': 'Prank call script stored successfully.'})

@app.route('/api/store-preferences', methods=['POST'])
def store_preferences():
    data = request.get_json()
    storeUserPreferences(data)
    return jsonify({'message': 'User preferences stored successfully.'})

@app.route('/api/schedule-call', methods=['POST'])
def schedule_call():
    data = request.get_json()
    storeScheduledCall(data)
    return jsonify({'message': 'Prank call scheduled successfully.'})

@app.route('/api/store-recording', methods=['POST'])
def store_recording():
    data = request.get_json()
    storeCallRecording(data)
    return jsonify({'message': 'Prank call recording stored successfully.'})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
```