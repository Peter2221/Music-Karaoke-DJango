from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from scipy.io import wavfile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import path
from django.conf import settings

# class VoiceAnalyzer:
#     def read_signal(self, path):
#         fs, y = wavfile.read(path)
#         return fs, y

#     def butter_lowpass(self, cutoff, fs, order=5):
#         nyq = 0.5 * fs
#         normal_cutoff = cutoff / nyq
#         b, a = butter(order, normal_cutoff, btype='low', analog=False)
#         return b, a

#     def butter_lowpass_filter(self, data, cutoff, fs, order=5):
#         b, a = self.butter_lowpass(cutoff, fs, order=order)
#         y = lfilter(b, a, data)
#         return y

#     def divide_signal_into_chunks(self, y, chunk_size):
#         return [y[i : i + chunk_size] for i in range(0, len(y), chunk_size)]

#     def get_frequencies(self, y, chunk_size):
#         freqs = []
#         for y_fourier in y:
#             y_fourier = fft(y_fourier)
#             y_fourier = y_fourier[0:int(chunk_size / 2)]
#             # index of max -> freq, * fs / step to get proper values
#             freq = np.argmax(abs(y_fourier)) * (fs / chunk_size)
#             freqs.append(freq)

#         return freqs

# def get_score(path1, path2):
#   CHUNK_SIZE = 4410
#   LOW_CUT_FREQ = 600

#   analyzer = VoiceAnalyzer()

#   fs, y = analyzer.read_signal(path1)
#   fs2, y2 = analyzer.read_signal(path2)

#   y = analyzer.butter_lowpass_filter(y, LOW_CUT_FREQ, fs)
#   y2 = analyzer.butter_lowpass_filter(y2, LOW_CUT_FREQ, fs2)

#   y = analyzer.divide_signal_into_chunks(y, CHUNK_SIZE)
#   y2 = analyzer.divide_signal_into_chunks(y2, CHUNK_SIZE)

#   freq = analyzer.get_frequencies(y, CHUNK_SIZE)
#   freq2 = analyzer.get_frequencies(y2, CHUNK_SIZE)

#   if(len(freq) > len(freq2)):
#       freq = freq[0:len(freq2)]
#   else:
#       freq2 = freq2[0:len(freq)]

#   mse = np.square(np.subtract(freq, freq2)).mean()

#   return mse


def save_score_to_db():
    # song_id, user_id, score

    pass


def join_path_with_base_dir(base_dir, filepath):
    if(filepath[0] == '/'):
        filepath = filepath[1:]
    return path.join(base_dir, filepath)


@csrf_exempt
def analysis(request):
    if request.method == "POST":
        audio_track_vocal_path = request.POST.get('audio_file_vocal')
        upload_file = request.FILES.get('audio_file')
        upload_file_path = default_storage.save(
            'media/audio_analysis/audio' + '.webm', ContentFile(upload_file.read()))

        BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

        audio_track_vocal_path = join_path_with_base_dir(
            BASE_DIR, audio_track_vocal_path)
        upload_file_path = join_path_with_base_dir(BASE_DIR, upload_file_path)

        fs, y = wavfile.read(audio_track_vocal_path)
        print(fs)
        print(y)

    return render(request, 'landing-page/landing.html')

    # save_score_to_db()
