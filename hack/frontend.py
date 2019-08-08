

class Frontend(object):
    """
    TODO: Clair
    Uses the api in the rest of the package to caption images.
    """

    def get_speech(self, jpeg_bytes, target_language):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: raw audio to be played on the devices WAV audio player
        """
        pass

    def get_caption(self, jpeg_bytes, target_language):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: a string (the caption for the image in the target language)
        """
        pass