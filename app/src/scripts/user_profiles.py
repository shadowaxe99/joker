class UserProfile:
    def __init__(self, username):
        self.username = username
        self.preferences = {}
        self.prank_history = []
        self.settings = {}

    def save_preferences(self, preferences):
        self.preferences = preferences

    def track_prank(self, prank):
        self.prank_history.append(prank)

    def manage_settings(self, settings):
        self.settings = settings