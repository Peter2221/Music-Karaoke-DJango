from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import wave
from .forms import Audio_to_play_form
from scipy.io import wavfile
import numpy as np

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

# Create your views here.
@csrf_exempt
def analysis(request):
  if request.method == "POST":

    print(request.FILES.get('audio_file'))

    upload_file = request.FILES['audio_file']
    print(upload_file.size)
    print(type(upload_file))

    # audio_test = wave.open('media/audio_files/ex.wav', 'wb')
    # #nchannels = audio_test.getnchannels()
    # nframes = audio_test.getnframes()
    # width = audio_test.getsampwidth()
    # framerate = audio_test.getframerate()

    # #print(nchannels)
    # print(nframes)
    # print(width)
    # print(framerate)
    audio = wave.open('media/audio_files/test.wav', 'wb')
    audio.setnchannels(1)
    audio.setnframes(100)
    audio.setsampwidth(1)
    audio.setframerate(8000)
    blob = upload_file.read()
    audio.writeframes(blob)
  return render(request, 'landing-page/landing.html')

  #save_score_to_db()
  #pass