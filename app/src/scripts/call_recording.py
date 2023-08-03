class CallRecording:
    def __init__(self):
        self.recordings = []

    def record_call(self, call):
        self.recordings.append(call)
        pass

    def save_recording(self, recording):
        self.recordings.append(recording)