class PrankCallRecordingPlayback:
    def __init__(self):
        self.recordings = []

    def add_recording(self, recording):
        self.recordings.append(recording)

    def play_recording(self, recording):
        print(f'Playing recording: {recording}')