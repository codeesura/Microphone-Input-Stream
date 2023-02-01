import time
import pyaudio

p = pyaudio.PyAudio()

while True:
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['name'] == 'microphone':
            mic_index = dev['index']

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=mic_index,
                    frames_per_buffer=1024)

    stream.stop_stream()
    stream.close()
    time.sleep(1)

p.terminate()
