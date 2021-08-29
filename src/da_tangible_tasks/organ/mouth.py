"""MOUTH MODULE FOR gTTS"""

from gtts import gTTS
from playsound import playsound
import os
        
class DeliveryArcadeAgentMouth():
    def talk_en(self, words):
            tts = gTTS(text = words, lang = 'en')
            tts.save('sample_1.mp3')
            playsound('sample_1.mp3', True)
            os.remove('sample_1.mp3')


    def talk_kr(self, words):
            tts = gTTS(text = words, lang = 'ko')
            tts.save('sample_1.mp3')
            playsound('sample_1.mp3', True)
            os.remove('sample_1.mp3')


    def talk_es(self, words):
            tts = gTTS(text = words, lang = 'es')
            tts.save('sample_1.mp3')
            playsound('sample_1.mp3', True)
            os.remove('sample_1.mp3') 

    def universal_talk(self, words, language):
        """Defined under language selection
            0 : ENGLISH
            1 : KOREAN
            2 : SPANISH
        """
        if language == 1:
            return self.talk_kr(words)
        elif language == 0:
            return self.talk_en(words)
        elif language == 2:
            return self.talk_es(words)