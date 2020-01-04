# -*- coding: utf-8 -*-
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

def drawGraph(datas):
    xorigin = np.frombuffer(datas, dtype="int16")
    x = xorigin / 3276800.0

    """
    plt.figure(figsize=(15,3))
    plt.plot(x)
    plt.show()
    """

    x = np.fft.fft(xorigin)
    absx = abs(x.real[:int(len(x)/2)])
    print(absx)

    prev = -1
    inc = True
    for idx, ab in enumerate(absx):
        if inc:
            if prev > ab:
                print(f"maxi{idx-1}->{prev}")
                inc = False
        else:
            if prev < ab:
                inc = True
        prev = ab
    """
    plt.figure(figsize=(15,3))
    plt.plot(abs(x.real[:int(len(x)/2)]))
    plt.show()
    """



FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 44100 
CHUNK = 2**11
RECORD_SECONDS = 1
DEVICE = 1

audio = pyaudio.PyAudio()


for x in range(0, audio.get_device_count()):
    # DEVICE INDEX
    print(audio.get_device_info_by_index(x))


stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index=DEVICE, 
        frames_per_buffer=CHUNK)
print ("start watch")
while True:
    data = stream.read(CHUNK)
    x = np.frombuffer(data, dtype="int16") / 32768.0

    if x.max() > 0.01:
        print("start record")
        frames = [data]
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        data = b''.join(frames)
        drawGraph(data)
        print("finish record & continue watch")

stream.stop_stream()
stream.close()
audio.terminate()

