class PrankCallChallenges:
    def __init__(self):
        self.challenges = {}

    def add_challenge(self, challenge):
        self.challenges.append(challenge)

    def get_challenges(self):
        return self.challenges