import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from scipy.io.wavfile import write
import soundfile as sf
import sys
# import pyaudio
import wave

num = sys.argv[1]
data, samplerate = sf.read('../SpeechRecognition/test/%s.wav'%num)
signalFFT = fft(data)
fft_range = np.arange(0,len(signalFFT),1)

count = 0
Yes = False
No = False

for i in range(int(1/10*len(signalFFT)),int(9/10*len(signalFFT))):
    if signalFFT[i]>10:
        count += 1

if count > 0:
    print("YES")
else:
    print("NO")

# data_range = np.arange(len(data))
# a = np.zeros(len(data))
# for i in range(len(data)):
#     a[i] = data[i] ** 2
# f = fft(a)
# plt.plot(data_range, f)
# plt.show()

