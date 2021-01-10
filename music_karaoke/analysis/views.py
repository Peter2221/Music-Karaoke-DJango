from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import JsonResponse

from os import path
import subprocess

from scipy.io import wavfile
from scipy.signal import butter, lfilter, freqz
from scipy.signal import stft
from scipy.fft import fft
import numpy as np


class VoiceAnalyzer:
    def read_signal(self, path):
        fs, y = wavfile.read(path)
        return fs, y

    def butter_lowpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y

    def divide_signal_into_chunks(self, y, chunk_size):
        return [y[i: i + chunk_size] for i in range(0, len(y), chunk_size)]

    def get_frequencies(self, y, fs, chunk_size):
        freqs = []
        for y_fourier in y:
            y_fourier = fft(y_fourier)
            y_fourier = y_fourier[0:int(chunk_size / 2)]
            # index of max -> freq, * fs / step to get proper values
            freq = np.argmax(abs(y_fourier)) * (fs / chunk_size)
            freqs.append(freq)

        return freqs

    def trim_frequencies(self, freq, freq2):
        if(len(freq) > len(freq2)):
            freq = freq[0:len(freq2)]
        else:
            freq2 = freq2[0:len(freq)]
        return freq, freq2


class VoiceScoreCalculator:
    def __init__(self):
        self.CHUNK_SIZE = 4410
        self.LOW_CUT_FREQ = 600
        self.analyzer = VoiceAnalyzer()

    def get_mse(self, path1, path2):
        fs, y = self.analyzer.read_signal(path1)
        fs2, y2 = self.analyzer.read_signal(path2)

        y = self.analyzer.butter_lowpass_filter(y, self.LOW_CUT_FREQ, fs)
        y2 = self.analyzer.butter_lowpass_filter(y2, self.LOW_CUT_FREQ, fs2)

        y = self.analyzer.divide_signal_into_chunks(y, self.CHUNK_SIZE)
        y2 = self.analyzer.divide_signal_into_chunks(y2, self.CHUNK_SIZE)

        freq = self.analyzer.get_frequencies(y, fs, self.CHUNK_SIZE)
        freq2 = self.analyzer.get_frequencies(y2, fs2, self.CHUNK_SIZE)

        freq, freq2 = self.analyzer.trim_frequencies(freq, freq2)
        mse = np.square(np.subtract(freq, freq2)).mean()
        return mse

    def get_score(self, path1, path2):
        mse = self.get_mse(path1, path2)

        if(mse <= 1000):
            return 100
        elif(mse <= 10000):
            return 50
        elif(mse <= 50000):
            return 25
        else:
            return 0


def save_score_to_db():
    # song_id, user_id, score

    pass


def join_path_with_base_dir(base_dir, filepath):
    if(filepath[0] == '/'):
        filepath = filepath[1:]
    return path.join(base_dir, filepath)


def convert_to_wav(filepath):
    # remove .webm
    output_path = filepath[:-5] + '.wav'
    command = ['ffmpeg', '-i', filepath, output_path]
    subprocess.run(command)
    return output_path


@csrf_exempt
def analysis(request):
    if request.method == "POST":
        audio_track_vocal_path = request.POST.get('audio_file_vocal')
        upload_file = request.FILES.get('audio_file')
        upload_file_path = default_storage.save(
            'media/audio_analysis/audio' + '.webm', ContentFile(upload_file.read()))

        # Get base directory path, in this case it's main project folder
        BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

        # Joining with paths for upload_file_path and audio_track_vocal_path
        audio_track_vocal_path = join_path_with_base_dir(
            BASE_DIR, audio_track_vocal_path)
        upload_file_path = join_path_with_base_dir(BASE_DIR, upload_file_path)

        # convert .webm file to .wav and save to the same dir
        converted_file_path = convert_to_wav(upload_file_path)

        # Getting score for source and user record
        voiceScoreCalculator = VoiceScoreCalculator()
        score = voiceScoreCalculator.get_score(
            audio_track_vocal_path, converted_file_path)

    return JsonResponse({'score': score})
