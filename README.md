
# Voice Recorder Application

## Overview

This is a simple Voice Recorder application implemented in Python using the Tkinter library for the graphical user interface and the sounddevice and wavio libraries for audio recording and saving.


## Features

- Record Button: Initiates the recording process.
- Stop Button: Stops the ongoing recording.
- Save Recording Button: Saves the recorded audio as a WAV file.
- Filename Entry: Allows the user to specify the filename for the recorded audio.
- Status Label: Displays the current status of the application, such as recording or recording stopped.




## Usage


1.Run the application by executing the script.

2.Click the "Record" button to start recording.

3.Click the "Stop" button to stop the recording.

4.Optionally, enter a desired filename in the entry field.

5.Click the "Save Recording" button to save the recorded audio as a WAV file.

## Dependencies

- sounddevice: Used for capturing audio input.
- wavio: Used for writing audio data to a WAV file.
- tkinter: Used for building the graphical user interface.
- numpy: Used for handling numerical data efficiently.
## Installation


```bash
  pip install sounddevice wavio numpy
```
 
## Running Test

To run tests, run the following command

```bash
  python voice_recorder.py
```

## Important Notes

- Ensure that you have a working microphone connected to your system.
- The recorded audio is saved in WAV format with a default filename of "recorded_audio.wav" (modifiable in the entry field).
- The sample rate is set to 44100 Hz, and the sample width is set to 24 bits.
