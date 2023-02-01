
# Microphone Input Stream


This code opens a PyAudio stream for the microphone input and closes it every second.

### Requirements

- PyAudio
- time

## Usage

```Python
python microphone_input_stream.py
```


## How it works

- The PyAudio object p is created.
- In an infinite loop:
    - The microphone device index is found by searching for the device with the name 'microphone'.
    - A PyAudio stream is opened for the microphone device with the given specifications: format paInt16, single channel, sample rate 44100 Hz, input enabled, using the microphone device index, and using 1024 frames per buffer.
    - The stream is stopped and closed.
    - The program waits for 1 second before repeating the loop.
- The PyAudio object is terminated at the end.

## Notes

- The loop runs continuously, so you need to interrupt the program to stop it (e.g. with `CTRL + C`).
- The sample rate and frames per buffer can be changed to match your requirements.
- Make sure that the 'microphone' device name matches the name of your microphone. You can change this to match the name of your microphone device.
- The input format `paInt16` is a signed 16-bit integer format. You can choose a different format if necessary.
- This code is only intended to demonstrate the basic usage of PyAudio for microphone input. You may need to modify it to fit your specific needs.

### Further reading

- PyAudio Documentation: https://people.csail.mit.edu/hubert/pyaudio/docs/
- PyAudio Tutorial: https://people.csail.mit.edu/hubert/pyaudio/docs/tutorial.html

