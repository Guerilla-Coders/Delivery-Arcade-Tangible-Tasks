from random import randint
from ..const.sound_consts import SoundEffectConstants

class RobotLine:
    def __init__(self):
        self.eng_greetings_list = [
            "Nice to meet you, I am here with your foods",
            "Finally! A worthy opponent! Our battle will be legendery!"
        ]

        self.eng_apologizes_list = [
            "I am so sorry for my mistakes! It won't happen again.",
            "My apologies. Could you please forgive me for that?"
        ]

        self.eng_appreciation_list = [
            "Thank you so much.",
            "Thanks. My owner also wants me to send his best appreciation to you."
        ]

        self.eng_yeild_inquiry_list = [
            "Sir, I am sorry to bother you, but could you step aside please?",
            "Sir, could you forgive me for asking you to step aside please? I am in a hurry."
        ]

        self.lines_list = [
            self.eng_greetings_list,
            self.eng_apologizes_list,
            self.eng_appreciation_list,
            self.eng_yeild_inquiry_list
        ]

    def pick_random_line(self, mode, random):
        current_lines = self.lines_list[mode]        
        index = randint(0,random)
        current_line = current_lines[index]
        return current_line

