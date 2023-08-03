from prank_call_recording import PrankCallRecording
from prank_call_recording_playback import PrankCallRecordingPlayback
from prank_call_sharing import PrankCallSharing

recording = PrankCallRecording('John', 'Jane', '5 minutes')
playback = PrankCallRecordingPlayback()
sharing = PrankCallSharing()

playback.add_recording(recording)
playback.play_recording(recording)

sharing.share_prank_call_on_social_media(recording, 'Twitter')
sharing.share_prank_call_via_email(recording, 'jane@example.com')