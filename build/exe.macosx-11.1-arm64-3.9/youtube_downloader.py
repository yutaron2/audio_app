import tkinter as tk
from pytube import YouTube
import threading
import traceback  # tracebackモジュールをインポート

class YoutubeDownloaderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("600x400")  # ウィンドウのサイズを変更

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=10)

        download_button = tk.Button(self, text="Download", command=self.start_download_thread)
        download_button.pack(pady=10)

        self.status_label = tk.Label(self, text="")
        self.status_label.pack(pady=10)

        # 新しいテキストウィジェットを追加
        self.error_output = tk.Text(self, height=10, width=50)
        self.error_output.pack(pady=10)

    def start_download_thread(self):
        threading.Thread(target=self.download_video).start()

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            self.status_label.config(text="Please enter a URL")
            return

        try:
            self.status_label.config(text="Downloading...")
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="downloads")
            self.status_label.config(text="Download complete!")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            # エラーの詳細をテキストウィジェットに表示
            error_detail = traceback.format_exc()
            self.error_output.insert(tk.END, error_detail)

if __name__ == "__main__":
    app = YoutubeDownloaderApp()
    app.mainloop()
