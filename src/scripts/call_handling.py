```python
from twilio.rest import Client
from src.voice_synthesis import generateVoice
from src.prank_call_customization import customizeScript

def initiateCall(userPreferences, scheduledCalls):
    # Your Account SID from twilio.com/console
    account_sid = "your_account_sid"
    # Your Auth Token from twilio.com/console
    auth_token  = "your_auth_token"

    client = Client(account_sid, auth_token)

    for call in scheduledCalls:
        if call['time'] == 'now':
            voice = generateVoice(userPreferences['voice'])
            script = customizeScript(userPreferences['script'], call['recipient'])
            
            message = client.calls.create(
                to=call['recipient'], 
                from_="your_twilio_number",
                url="http://twimlets.com/echo?Twiml=<Response><Say voice='{}'>{}</Say></Response>".format(voice, script)
            )

            print("Prank call initiated: ", message.sid)
```