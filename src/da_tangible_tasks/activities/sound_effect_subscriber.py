#!/usr/bin/env python3

import rospy
# from ..psuedo_msg.psuedo_sound_effects import sound_effects
from turtlebot3_bringup.msg import sound_effect
from ..const.sound_consts import SoundEffectConstants


class SoundEffectSubscriber:
    def __init__(self):
        # self.mode = SoundEffectConstants.DEFAULT_MODE
        self.mode = None
        self.random = SoundEffectConstants.DEFAULT_RANDOM
        self.language = SoundEffectConstants.DEFAULT_LANGUAGE

        self.sound_effect_format = sound_effect()

    def fetch_sound_effect_data(self) -> None:
        sound_effect_data: sound_effect = rospy.wait_for_message('sound_effect', sound_effect)
        self.mode = sound_effect_data.mode
        self.random = sound_effect_data.random
        self.language = sound_effect_data.language

    def get_information(self):
        self.fetch_sound_effect_data()
        sound_effect_dict = {
            'mode': self.mode,
            'random': self.random,
            'language': self.language
        }
        return sound_effect_dict
