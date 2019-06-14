import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy.fftpack import fft, ifft
from scipy.io.wavfile import write

data, samplerate = sf.read('../SpeechRecognition/test/n4.wav')
signalFFT = fft(data)
fft_range = np.arange(0,len(signalFFT),1)

data2, samplerate = sf.read('../SpeechRecognition/test/n5.wav')
signalFFT_2 = fft(data2)
fft_range_2 = np.arange(0,len(signalFFT_2),1)

data3, samplerate = sf.read('../SpeechRecognition/test/n6.wav')
signalFFT_3 = fft(data3)
fft_range_3 = np.arange(0,len(signalFFT_3),1)


data4, samplerate = sf.read('../SpeechRecognition/test/n7.wav')
signalFFT_4 = fft(data4)
fft_range_4 = np.arange(0,len(signalFFT_4),1)


chart1 = plt.subplot(221)
plt.plot(fft_range,signalFFT )


chart1 = plt.subplot(222)
plt.plot(fft_range_2,signalFFT_2 )


chart1 = plt.subplot(223)
plt.plot(fft_range_3,signalFFT_3 )


chart1 = plt.subplot(224)
plt.plot(fft_range_4,signalFFT_4 )

plt.show()



data, samplerate = sf.read('../SpeechRecognition/test/y1.wav')
signalFFT = fft(data)
fft_range = np.arange(0,len(signalFFT),1)

data2, samplerate = sf.read('../SpeechRecognition/test/y2.wav')
signalFFT_2 = fft(data2)
fft_range_2 = np.arange(0,len(signalFFT_2),1)

data3, samplerate = sf.read('../SpeechRecognition/test/y3.wav')
signalFFT_3 = fft(data3)
fft_range_3 = np.arange(0,len(signalFFT_3),1)


data4, samplerate = sf.read('../SpeechRecognition/test/y4.wav')
signalFFT_4 = fft(data4)
fft_range_4 = np.arange(0,len(signalFFT_4),1)


chart1 = plt.subplot(221)
plt.plot(fft_range,signalFFT)


chart1 = plt.subplot(222)
plt.plot(fft_range_2,signalFFT_2 )


chart1 = plt.subplot(223)
plt.plot(fft_range_3,signalFFT_3 )


chart1 = plt.subplot(224)
plt.plot(fft_range_4,signalFFT_4 )

plt.show()