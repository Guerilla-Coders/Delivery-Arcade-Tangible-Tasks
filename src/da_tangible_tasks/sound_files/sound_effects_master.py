#!/usr/bin/env python3

from .sound_effects_subscriber import SoundEffectSubscriber
from ..organ.mouth import universal_talk
from temporary_sound_files import *
from ..const.sound_consts import SoundEffectConstants
import rospy

class SoundEffectMaster:
    def __init__(self):
        # self.mode = SoundEffectConstants.DEFAULT_MODE
        self.mode = None
        self.random = SoundEffectConstants.DEFAULT_RANDOM
        self.language = SoundEffectConstants.DEFAULT_LANGUAGE
        self.subscriber = SoundEffectSubscriber()    
        self.mouth = universal_talk()

    def get_sound_effects_info(self):
        sound_effects_info = self.subscriber.get_information()
        self.mode = sound_effects_info['mode']
        self.random = sound_effects_info['random']
        self.language = sound_effects_info['language']

    def get_ready_for_speech(self):
        self.robotline = RobotLine().pick_random_line(self.mode, self.random)

    def say_it(self):
        self.mouth(self.robotline, self.language)

    def run_sound(self):
        self.get_sound_effects_info()
        self.get_ready_for_speech()
        self.say_it()
    