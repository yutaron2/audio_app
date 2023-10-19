import os
import tkinter as tk
from moviepy.video.io.VideoFileClip import VideoFileClip
from helpers.file_selector import FileSelector

class AudioExtractorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Audio Extractor")
        self.geometry("300x100")

        extract_button = tk.Button(self, text="Extract Audio", command=self.extract_audio)
        extract_button.pack(pady=20)

    def extract_audio(self):
        video_filepath = FileSelector().select_file()
        if video_filepath:  # Check if a file was selected
            audio_filepath = os.path.splitext(video_filepath)[0] + "_audio.mp3"
            self._extract_audio(video_filepath, audio_filepath)

    def _extract_audio(self, video_filepath, audio_filepath):
        video_clip = VideoFileClip(video_filepath)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_filepath, codec='mp3')
        video_clip.reader.close()
        audio_clip.reader.close()

if __name__ == "__main__":
    app = AudioExtractorApp()
    app.mainloop()
