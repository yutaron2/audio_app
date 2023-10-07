import tkinter as tk

class AudioPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Audio Player")
        self.geometry("300x100")

        play_button = tk.Button(self, text="Play", command=self.play_audio)
        play_button.pack(pady=10)

        stop_button = tk.Button(self, text="Stop", command=self.stop_audio)
        stop_button.pack(pady=10)

    def play_audio(self):
        # ここに音声を再生するコードを書く
        pass

    def stop_audio(self):
        # ここに音声を停止するコードを書く
        pass
