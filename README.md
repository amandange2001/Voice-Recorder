Voice Recorder Application
Overview
This is a simple Voice Recorder application implemented in Python using the Tkinter library for the graphical user interface and the sounddevice and wavio libraries for audio recording and saving.

Features
1.Record Button: Initiates the recording process.
2.Stop Button: Stops the ongoing recording.
3.Save Recording Button: Saves the recorded audio as a WAV file.
4.Filename Entry: Allows the user to specify the filename for the recorded audio.
5.Status Label: Displays the current status of the application, such as recording or recording stopped.

Usage
1.Run the application by executing the script.
2.Click the "Record" button to start recording.
3.Click the "Stop" button to stop the recording.
4.Optionally, enter a desired filename in the entry field.
5.Click the "Save Recording" button to save the recorded audio as a WAV file.

Dependencies
1.sounddevice: Used for capturing audio input.
2.wavio: Used for writing audio data to a WAV file.
3.tkinter: Used for building the graphical user interface.
4.numpy: Used for handling numerical data efficiently.

Installation
pip install sounddevice wavio numpy

How to Run
python voice_recorder.py

Important Notes
1.Ensure that you have a working microphone connected to your system.
2.The recorded audio is saved in WAV format with a default filename of "recorded_audio.wav" (modifiable in the entry field).
3.The sample rate is set to 44100 Hz, and the sample width is set to 24 bits.
4.Feel free to explore and enhance the application according to your needs!

Recording
https://github.com/amandange2001/Voice-Recorder/assets/100614486/9e85734b-0012-4020-838e-1d41f6c58d1b

