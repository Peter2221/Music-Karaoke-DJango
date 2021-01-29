from django.test import TestCase
from .views import VoiceAnalyzer
from .views import VoiceScoreCalculator
from .views import convert_to_wav

from scipy.io import wavfile
from scipy.signal import butter, lfilter, freqz
from scipy.signal import stft
from scipy.fft import fft
import numpy as np
import os


class VoiceAnalyzerTestCase(TestCase):
    def setUp(self):
        self.voiceAnalyzer = VoiceAnalyzer()
        self.chunk_size = 1024
        self.filepath_wav = os.path.dirname(
            __file__) + '/test_files/audio_test.wav'
        self.filepath_wav2 = os.path.dirname(
            __file__) + '/test_files/audio_test2.wav'

    def test_signal_is_read_from_dir(self):
        """
        File in .wav format should be properly read
        and sample frequency and signal numpy array should be returned
        """
        fs, y = self.voiceAnalyzer.read_signal(self.filepath_wav)
        self.assertGreater(fs, 0)
        self.assertGreater(len(y), 0)

    def test_signal_is_divided_into_chunks(self):
        """
        Signal should be divided into equal chunks (except for the last chunk that can have different length)
        """
        fs, y = self.voiceAnalyzer.read_signal(self.filepath_wav)
        y = self.voiceAnalyzer.divide_signal_into_chunks(y, self.chunk_size)
        self.assertEqual(len(y[0]), self.chunk_size)
        self.assertGreater(len(y[-1]), 0)

    def test_get_frequencies(self):
        """
        For every chunk of signal maximum frequency is counted
        based of fft
        """
        fs, y = self.voiceAnalyzer.read_signal(self.filepath_wav)
        y = self.voiceAnalyzer.divide_signal_into_chunks(y, self.chunk_size)
        freqs = self.voiceAnalyzer.get_frequencies(y, fs, self.chunk_size)
        self.assertGreater(len(freqs), 0)

    def test_trim_frequencies_arrays(self):
        """
        Output frequencies lists should be the same size
        """
        fs, y = self.voiceAnalyzer.read_signal(self.filepath_wav)
        fs2, y2 = self.voiceAnalyzer.read_signal(self.filepath_wav2)
        y = self.voiceAnalyzer.divide_signal_into_chunks(y, self.chunk_size)
        y2 = self.voiceAnalyzer.divide_signal_into_chunks(y2, self.chunk_size)
        freqs = self.voiceAnalyzer.get_frequencies(y, fs, self.chunk_size)
        freqs2 = self.voiceAnalyzer.get_frequencies(y2, fs2, self.chunk_size)
        freqs, freqs2 = self.voiceAnalyzer.trim_frequencies(freqs, freqs2)
        self.assertEqual(len(freqs), len(freqs2))


class VoiceScoreCalculatorTestCase(TestCase):
    def setUp(self):
        self.voiceScoreCalculator = VoiceScoreCalculator()
        self.filepath_wav = os.path.dirname(
            __file__) + '/test_files/audio_test.wav'
        self.filepath_wav2 = os.path.dirname(
            __file__) + '/test_files/audio_test2.wav'

    def test_get_score(self):
        """
        Should return score for 2 .wav files
        """
        score = self.voiceScoreCalculator.get_score(
            self.filepath_wav, self.filepath_wav2)
        self.assertGreaterEqual(score, 0)


class ConvertWavFileTestCase(TestCase):
    def setUp(self):
        self.filepath_webm = os.path.dirname(
            __file__) + '/test_files/audio_test_web.webm'
        self.filepath_webm_converted = os.path.dirname(
            __file__) + '/test_files/audio_test_web.wav'

    def test_convert_from_webm_to_wav(self):
        """
        Should convert .webm file to .wav and save in the same dir
        """
        convert_to_wav(self.filepath_webm)
        does_exist = os.path.exists(self.filepath_webm_converted)
        self.assertTrue(does_exist)

    def tearDown(self):
        os.remove(self.filepath_webm_converted)
        return super().tearDown()
