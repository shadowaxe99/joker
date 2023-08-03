class PrankCategories:
    def __init__(self):
        self.categories = {}

    def add_prank_to_category(self, prank, category):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(prank)

    def get_pranks_in_category(self, category):
        if category in self.categories:
            return self.categories[category]
        else:
            return []