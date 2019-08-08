import hack.constants


class Translator(object):
    """
    Translates from english to french, and german
    """

    def translate(self, english_message, target_language):
        """
        :param english_message: a string
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: a tuple of a string
        """
        self.message = english_message
        self.target_language = target_language

        if target_language == 'fr':
            return self._to_french(self.message)
        elif target_language == 'de':
            return self._to_german(self.message)
        else: 
            print("Please enter 'fr' or 'de' only.")
            return None

    def _to_french(self, english_message):
        """
        :param english_message: a string that is padded to 140 characters
        :param actual_length: an integer for the actual unpadded string length
        :return: a tuple of a string that is padded to 140 characters (translated sentence),
                 and an integer (the length of the actual string)
        """
        return fr_translation

    def _to_german(self, english_message):
        """
        :param english_message: a string that is padded to 140 characters
        :param actual_length: an integer for the actual unpadded string length
        :return: a tuple of a string that is padded to 140 characters (translated sentence),
                 and an integer (the length of the actual string)
        """
        return de.translation