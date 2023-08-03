from prank_call_recording_playback import PrankCallRecordingPlayback
from prank_call_sharing import PrankCallSharing

class PrankCallManager:
    def __init__(self):
        self.recording_playback = PrankCallRecordingPlayback()
        self.sharing = PrankCallSharing()

    def add_recording(self, recording):
        self.recording_playback.add_recording(recording)

    def play_recording(self, recording):
        self.recording_playback.play_recording(recording)

    def share_prank_call_on_social_media(self, prank_call, platform):
        self.sharing.share_prank_call_on_social_media(prank_call, platform)

    def share_prank_call_via_email(self, prank_call, email):
        self.sharing.share_prank_call_via_email(prank_call, email)