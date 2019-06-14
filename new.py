from scipy.io import wavfile as wav
from scipy.fftpack import fft
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt


# audio config params
FORMAT = pyaudio.paInt16  # format of sampling 16 bit int
CHANNELS = 1  # number of channels it means number of sample in every sampling
RATE = 44100  # number of sample in 1 second sampling
CHUNK = 1024  # length of every chunk
RECORD_SECONDS = 2  # time of recording in seconds
WAVE_OUTPUT_FILENAME = "file.wav"  # file name

classes = []
audio = pyaudio.PyAudio()
list_fft = []
count = 0
print("\n\n\n\n\n")
while True:
    # start Recording
    print("sart new recording...")
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    # print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()

    # storing voice
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    rate, data = wav.read('file.wav')

    min_freq = 10000
    max_freq = len(data) - 10000
    signalFFT = np.fft.fft(data)
    f = np.absolute(signalFFT)
    num = 0 
    # 70000 ->100000
    mute_count = 0
    for i in range(min_freq, max_freq):
        if f[i] > 70000:
            num += 1
    if num >0:
        print("Yes")
        classes.append("Yes")

    else:
        for i in range(1000,min_freq):
            if f[i] > 70000:
                mute_count += 1
            else:
                pass
        print(mute_count)
        if mute_count <100 :
            print("Mute")
            classes.append("Mute")
        else:
            print("No")
            classes.append("No")

    list_fft.append(f)
    count += 1
    if count == 4:
        break

# print("VISUALIZATION\n")
# a = input("Do you eant to plot 4 first data?1/2")
# if a == "1":
fft_range =np.arange(len(data))
chart1 = plt.subplot(221)
plt.plot(fft_range,list_fft[0])
plt.title(classes[0])

chart1 = plt.subplot(222)
plt.plot(fft_range, list_fft[1])
plt.title(classes[1])

chart1 = plt.subplot(223)
plt.plot(fft_range, list_fft[2])
plt.title(classes[2])

chart1 = plt.subplot(224)
plt.plot(fft_range, list_fft[3])
plt.title(classes[3])

plt.show()
# else:
#     pass
