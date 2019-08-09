from hack.caption_utils.pythia_wrapper import PythiaWrapper
import hack.constants as constants


class Captioner(object):
    """
    Todo: Brandon
    """
    
    def __init__(self):
        """
        :member wrapper: the backend captioning algorithm built using Pythia.
        """
        self.wrapper = PythiaWrapper()

    def caption(self, jpeg_bytes):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :return: a sentence in english (all lower case) with (20) words max.
        """
        with open(constants.TEMP_FILE, "wb") as f:
            f.write(jpeg_bytes)
        tokens = self.wrapper.predict(constants.TEMP_FILE)
        return self.wrapper.caption_processor(tokens.tolist()[0])["caption"]
