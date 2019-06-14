import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt
import sys
# read audio samples
input1 = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]
input4 = sys.argv[4]

input_data = read("../SpeechRecognition/test/%s.wav"%input1)
input_data_2 = read("../SpeechRecognition/test/%s.wav"%input2)
input_data_3 = read("../SpeechRecognition/test/%s.wav"%input3)
input_data_4 = read("../SpeechRecognition/test/%s.wav"%input4)

audio = input_data[1]
# apply a Hanning window
window = hann(1024)
audio = audio[0:1024]*window
# fft
mags = abs(rfft(audio))
# convert to dB
mags = 20*scipy.log10(mags)
# normalise to 0 dB max
mags -= max(mags)
chart1 = plt.subplot(221)
plt.plot(mags)
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
plt.title("%s Spectrum"%input1)
"***************************************"
audio_2 = input_data_2[1]
window_2 = hann(1024)
audio_2 = audio_2[0:1024]*window_2
mags_2 = abs(rfft(audio_2))
mags_2 = 20*scipy.log10(mags_2)
mags_2 -= max(mags_2)
chart1 = plt.subplot(222)
plt.plot(mags_2)
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
plt.title("%s Spectrum"%input2)
"*****************************************"
audio_3 = input_data_3[1]
window_3 = hann(1024)
audio_3 = audio_3[0:1024]*window_3
mags_3 = abs(rfft(audio_3))
mags_3 = 20*scipy.log10(mags_3)
mags_3 -= max(mags_3)
chart1 = plt.subplot(223)
plt.plot(mags_3)
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
plt.title("%s Spectrum"%input3)
"****************************************"
audio_4 = input_data_4[1]
window_4 = hann(1024)
audio_4 = audio_4[0:1024]*window_4
mags_4 = abs(rfft(audio_4))
mags_4 = 20*scipy.log10(mags_4)
mags_4 -= max(mags_4)
chart1 = plt.subplot(224)
plt.plot(mags_4)
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
plt.title("%s Spectrum"%input4)
"******************************************"
plt.show()
