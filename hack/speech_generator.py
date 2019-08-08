import hack.constants


class SpeechGenerator(object):

    def generate(self, message, target_language):
        """
        :param message: a string message in the target_language
        :param target_language: an integer corresponding to the chosen language
        :return: raw audio that can be played my a WAV audio player
        """