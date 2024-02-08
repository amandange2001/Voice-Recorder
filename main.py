import sounddevice as sd
import wavio
import tkinter as tk
from tkinter import ttk
import numpy as np 


class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.record_button = ttk.Button(root, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.save_button = ttk.Button(root, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.filename_entry = ttk.Entry(root, width=30)
        self.filename_entry.insert(0, "recorded_audio")
        self.filename_entry.pack(pady=10)

        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=10)

        self.frames = []
        self.stream = None

    def start_recording(self):
        self.frames = []  # Clear previous frames
        self.stream = sd.InputStream(callback=self.callback)
        self.stream.start()
        self.record_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL
        self.save_button["state"] = tk.DISABLED
        self.status_label["text"] = "Recording..."

    def stop_recording(self):
        if self.stream:
            self.stream.stop()
            self.stream.close()
            self.record_button["state"] = tk.NORMAL
            self.stop_button["state"] = tk.DISABLED
            self.save_button["state"] = tk.NORMAL
            self.status_label["text"] = "Recording stopped."

    def save_recording(self):
        if self.frames:
            filename = self.filename_entry.get() + ".wav"
            wavio.write(filename, np.array(self.frames), 44100, sampwidth=3)
            self.status_label["text"] = f"Recording saved as {filename}"
        else:
            self.status_label["text"] = "No recording to save."

    def callback(self, indata, frames, time, status):
        if status:
            print(status, flush=True)
        self.frames.extend(indata.copy())

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
