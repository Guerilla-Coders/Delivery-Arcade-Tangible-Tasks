class SoundEffectConstants:
    """mode"""
    GREETING = 0
    APOLOGY = 1
    APPRECIATION = 2
    YEILD = 3
    PIGEON = 4

    DEFAULT_MODE = 0

    """stochasiticity"""
    RANDOM = 1

    DEFAULT_RANDOM = 1

    """language"""
    ENGLISH = 0
    KOREAN = 1
    SPANISH = 2

    DEFAULT_LANGUAGE = 0  # default language : english


class ActionConstants:
    lid_open = "OPEN"
    lid_close = "CLOSE"
