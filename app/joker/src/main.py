from prank_call_manager import PrankCallManager
from prank_call_recording import PrankCallRecording

manager = PrankCallManager()

recording1 = PrankCallRecording('John', 'Jane', '5 minutes')
recording2 = PrankCallRecording('Mike', 'Sarah', '3 minutes')

manager.add_recording(recording1)
manager.add_recording(recording2)

manager.play_recording(recording1)
manager.play_recording(recording2)

manager.share_prank_call_on_social_media(recording1, 'Twitter')
manager.share_prank_call_on_social_media(recording2, 'Facebook')

manager.share_prank_call_via_email(recording1, 'example1@example.com')
manager.share_prank_call_via_email(recording2, 'example2@example.com')