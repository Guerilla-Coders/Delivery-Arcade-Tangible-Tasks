#!/usr/bin/env python3

import rospy
# from ..psuedo_msg.psuedo_sound_effects import sound_effects
from turtlebot3_bringup.msg import sound_effects
from ..const.sound_consts import SoundEffectConstants

class SoundEffectSubscriber:
    def __init__(self):
        # self.mode = SoundEffectConstants.DEFAULT_MODE
        self.mode = None
        self.random = SoundEffectConstants.DEFAULT_RANDOM
        self.language = SoundEffectConstants.DEFAULT_LANGUAGE

        self.sound_effects_format = sound_effects()

    def fetch_sound_effects_data(self) -> None:
        sound_effects_data : sound_effects = rospy.wait_for_message('sound_effects', sound_effects)
        self.mode = sound_effects_data.mode
        self.random = sound_effects_data.random
        self.language = sound_effects_data.language

    def get_information(self):
        self.fetch_sound_effects_data()
        sound_effects_dict = {
            'mode' : self.mode,
            'random' : self.random,
            'language' : self.language
        }
        return sound_effects_dict
