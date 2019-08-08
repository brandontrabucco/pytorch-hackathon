import hack.constants
import numpy as np


class SpeechGenerator(object):
    """
    TODO: Rishabh
    Converts strings in English, French, or German to WAV audio.
    """

    def generate(self, message, target_language):
        """
        :param message: a string message in the target_language
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: raw audio that can be played my a WAV audio player
        """
        return np.zeros([1, 1])
