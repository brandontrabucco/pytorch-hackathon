from hack.captioner import Captioner
from hack.translator import Translator
from hack.speech_synthesizer import SpeechSynthesizer
import hack.constants as constants


class Frontend(object):
    """
    Uses the api in the rest of the package to caption images.
    """
    
    def __init__(self):
        """
        Builds each module of the backend.
        """
        self.captioner = Captioner()
        self.translator = Translator()
        self.speech_synthesizer = SpeechSynthesizer()

    def get_speech(self, jpeg_bytes, target_language):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: raw audio to be played on the devices WAV audio player
        """
        caption = self.captioner.caption(jpeg_bytes)
        translated_sentence = self.translator.translate(caption, target_language)
        wav_audio = self.speech_synthesizer.synthesize(translated_sentence, constants.ENGLISH)
        return wav_audio

    def get_caption(self, jpeg_bytes, target_language):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: a string (the caption for the image in the target language)
        """
        caption = self.captioner.caption(jpeg_bytes)
        translated_sentence = self.translator.translate(caption, target_language)
        return translated_sentence

    def get_speech_and_caption(self, jpeg_bytes, target_language):
        """
        :param jpeg_bytes: bytes for a jpeg image to be captioned (might need to specify an encoding)
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: a tuple of a string (the caption for the image in the target language), and
                 raw audio to be played on the devices WAV audio player
        """
        caption = self.captioner.caption(jpeg_bytes)
        translated_sentence = self.translator.translate(caption, target_language)
        wav_audio = self.speech_synthesizer.synthesize(translated_sentence, constants.ENGLISH)
        return translated_sentence, wav_audio
    