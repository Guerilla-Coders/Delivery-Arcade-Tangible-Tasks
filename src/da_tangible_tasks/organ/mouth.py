"""MOUTH MODULE FOR gTTS"""

from gtts import gTTS
# from playsound import playsound
from da_tangible_tasks.const.sound_consts import SoundEffectConstants
import os


class DeliveryArcadeAgentMouth:
    def __init__(self):
        self.lang_dict = {
            SoundEffectConstants.ENGLISH: 'en',
            SoundEffectConstants.KOREAN: 'ko',
            SoundEffectConstants.SPANISH: 'es'
        }

    def talk(self, words, language):
        """Defined under language selection
            0 : ENGLISH (en)
            1 : KOREAN (ko)
            2 : SPANISH (es)
        """
        tts = gTTS(text=words, lang=self.lang_dict[language])
        tts.save('./sample_1.mp3')
        # playsound('sample_1.mp3', True)
        os.system('chmod +x ./sample_1.mp3')
        # os.system('vlc ./sample_1.mp3 vlc://quit')
        os.system('cvlc ./sample_1.mp3 vlc://quit')
        os.remove('./sample_1.mp3')
