class Soundboard:
    def __init__(self):
        self.sound_effects = []

    def add_sound_effect(self, sound_effect):
        self.sound_effects.append(sound_effect)

    def play_sound_effect(self, sound_effect):
        print(f'Playing sound effect: {sound_effect}')
        pass