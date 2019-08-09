import hack.constants as constants

import sys
#sys.path.append(constants.WAVEGLOW_PATH)
sys.path.append(constants.TACOTRON_PATH)
import numpy as np
import torch

from hparams import create_hparams
from model import Tacotron2
from layers import TacotronSTFT, STFT
from audio_processing import griffin_lim
from train import load_model
from text import text_to_sequence
from denoiser import Denoiser


class SpeechSynthesizer(object):
    """
    TODO: Rishabh
          Converts strings in English to WAV audio.
    """
    
    def __init__(self):
        hparams = create_hparams()
        hparams.sampling_rate = 22050
        checkpoint_path = constants.TACOTRON_PT
        self.model = load_model(hparams)
        self.model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
        _ = self.model.cuda().eval().half()
        waveglow_path = constants.WAVEGLOW_PT
        self.waveglow = torch.load(waveglow_path)['model']
        self.waveglow.cuda().eval().half()
        for k in self.waveglow.convinv:
            k.float()
        self.denoiser = Denoiser(self.waveglow)

    def synthesize(self, message, target_language):
        """
        :param message: a string message in the target_language
        :param target_language: an integer corresponding to the chosen language (from hack.constants)
        :return: raw audio that can be played my a WAV audio player
        """
        sequence = np.array(text_to_sequence(message, ['english_cleaners']))[None, :]
        sequence = torch.autograd.Variable(
            torch.from_numpy(sequence)).cuda().long()
        mel_outputs, mel_outputs_postnet, _, alignments = self.model.inference(sequence)
        with torch.no_grad():
            audio = self.waveglow.infer(mel_outputs_postnet, sigma=0.666)
            audio_denoised = self.denoiser(audio, strength=0.01)[:, 0]
        return audio_denoised[0].data.cpu().numpy()
