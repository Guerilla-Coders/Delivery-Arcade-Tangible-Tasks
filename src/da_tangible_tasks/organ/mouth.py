"""MOUTH MODULE FOR gTTS"""

from gtts import gTTS
# from playsound import playsound
from da_tangible_tasks.const.sound_consts import SoundEffectConstants
import os


class DeliveryArcadeAgentMouth:
    alias = {
        "EN": "en",
        "KR": "ko",
        "ES": "es"
    }

    def talk(self, words, language):
        tts = gTTS(text=words, lang=self.alias[language])
        tts.save('./sample_1.mp3')
        # playsound('sample_1.mp3', True)
        os.system('chmod +x ./sample_1.mp3')
        # os.system('vlc ./sample_1.mp3 vlc://quit')
        os.system('cvlc ./sample_1.mp3 vlc://quit')
        os.remove('./sample_1.mp3')
