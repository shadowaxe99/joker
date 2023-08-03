class PrankSearch:
    def __init__(self):
        self.pranks = {}

    def add_prank(self, prank, keywords):
        self.pranks[prank] = keywords

    def search_by_keyword(self, keyword):
        results = []
        for prank, keywords in self.pranks.items():
            if keyword in keywords:
                results.append(prank)
        return results

    def search_by_category(self, category):
        results = []
        for prank, keywords in self.pranks.items():
            if category in keywords:
                results.append(prank)
        return results