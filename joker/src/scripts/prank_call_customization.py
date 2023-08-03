class PrankCustomization:
    def __init__(self):
        self.voices = ['Voice 1', 'Voice 2', 'Voice 3']
        self.scripts = ['Script 1', 'Script 2', 'Script 3']
        self.sound_effects = ['Sound Effect 1', 'Sound Effect 2', 'Sound Effect 3']

    def customize_voice(self, voice):
        self.voice = voice
        pass

    def customize_script(self, script):
        self.script = script
        pass

    def add_sound_effect(self, sound_effect):
        self.sound_effects.append(sound_effect)
        pass