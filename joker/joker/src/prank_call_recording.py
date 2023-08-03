class PrankCallRecording:
    def __init__(self, caller, recipient, duration):
        self.caller = caller
        self.recipient = recipient
        self.duration = duration

    def __str__(self):
        return f'Caller: {self.caller}, Recipient: {self.recipient}, Duration: {self.duration}'