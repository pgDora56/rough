# -*- coding: utf-8 -*-
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 44100 
CHUNK = 2**11
RECORD_SECONDS = 3 
DEVICE = 1

audio = pyaudio.PyAudio()


for x in range(0, audio.get_device_count()):
    # DEVICE INDEX
    print(audio.get_device_info_by_index(x))


stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index=DEVICE, 
        frames_per_buffer=CHUNK)
print ("start record")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finish record")

stream.stop_stream()
stream.close()
audio.terminate()

datas = b''.join(frames)

# 以上音声記録
# 以下描画

xorigin = np.frombuffer(datas, dtype="int16")
x = xorigin / 3276800.0

plt.figure(figsize=(15,3))
plt.plot(x)
plt.show()

x = np.fft.fft(xorigin)

plt.figure(figsize=(15,3))
plt.plot(abs(x.real[:int(len(x)/2)]))
plt.show()
