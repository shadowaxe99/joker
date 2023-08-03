class PrankCallHistory:
    def __init__(self):
        self.history = []

    def add_prank_call(self, prank_call):
        self.history.append(prank_call)

    def get_prank_call_history(self):
        return self.history