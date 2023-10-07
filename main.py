import tkinter as tk
from audio_extractor import AudioExtractorApp
from youtube_downloader import YoutubeDownloaderApp
from audio_player import AudioPlayerApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main App")
        self.geometry("300x150")

        extract_button = tk.Button(self, text="Extract Audio", command=self.launch_audio_extractor)
        extract_button.pack(pady=10)

        download_button = tk.Button(self, text="Download Video", command=self.launch_youtube_downloader)
        download_button.pack(pady=10)

        player_button = tk.Button(self, text="Play Audio", command=self.launch_audio_player)
        player_button.pack(pady=10)

    def launch_audio_extractor(self):
        AudioExtractorApp().mainloop()

    def launch_youtube_downloader(self):
        YoutubeDownloaderApp().mainloop()

    def launch_audio_player(self):
        AudioPlayerApp().mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
