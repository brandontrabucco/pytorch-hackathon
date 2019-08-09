from hack.caption_utils.pythia_wrapper import PythiaWrapper


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
        tokens = self.wrapper.predict(jpeg_bytes)
        return self.wrapper.caption_processor(tokens.tolist()[0])["caption"]
