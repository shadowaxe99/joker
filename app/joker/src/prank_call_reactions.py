class PrankCallReactions:
    def __init__(self):
        self.reactions = []

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def get_reactions(self):
        return self.reactions