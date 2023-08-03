```python
from google.cloud import texttospeech

def generateVoice(text, voice_name='en-US-Wavenet-F', language_code='en-US'):
    """
    Function to generate voice from text using Google Text-to-Speech API
    """
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code, 
        name=voice_name
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    return response.audio_content
```