import hack.constants


class Translator(object):
    """
    Translates from english to french, and german
    """

    def translate(self, english_message, target_language):
        """
        :param english_message: a string
        :param target_language: an integer for the actual unpadded string length
        :return: a tuple of a string
        """
        actual_length = len(english_message)
        english_message = english_message[:hack.constants.MAX_PADDING]
        if actual_length < hack.constants.MAX_PADDING:
            english_message += " " * (actual_length - hack.constants.MAX_PADDING)
        if target_language == hack.constants.GERMAN:
            final_message, length = self._to_german(english_message, actual_length)
            return final_message[:length]
        if target_language == hack.constants.FRENCH:
            final_message, length = self._to_french(english_message, actual_length)
            return final_message[:length]

    def _to_french(self, english_message, actual_length):
        """
        :param english_message: a string that is padded to 140 characters
        :param actual_length: an integer for the actual unpadded string length
        :return: a tuple of a string that is padded to 140 characters (translated sentence),
                 and an integer (the length of the actual string)
        """
        return "", 0

    def _to_german(self, english_message, actual_length):
        """
        :param english_message: a string that is padded to 140 characters
        :param actual_length: an integer for the actual unpadded string length
        :return: a tuple of a string that is padded to 140 characters (translated sentence),
                 and an integer (the length of the actual string)
        """
        return "", 0
