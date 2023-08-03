class PrankCallScripts:
    def __init__(self):
        self.scripts = {}

    def add_script(self, script, prank):
        if prank not in self.scripts:
            self.scripts[prank] = []
        self.scripts[prank].append(script)

    def get_scripts_for_prank(self, prank):
        if prank in self.scripts:
            return self.scripts[prank]
        else:
            return []