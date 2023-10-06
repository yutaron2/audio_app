import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def select_file():
    """
    Open a file dialog and return the selected file's path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

def extract_audio(video_filepath, audio_filepath):
    """
    Extract audio from a video file and save it as an mp3 file.

    Parameters:
    - video_filepath: str, path to the input video file
    - audio_filepath: str, path to the output audio file
    """
    video_clip = VideoFileClip(video_filepath)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_filepath, codec='mp3')
    video_clip.reader.close()
    audio_clip.reader.close()

# Example usage:
video_filepath = select_file()  # Select the video file using a file dialog
audio_filepath = "output_audio.mp3"  # Specify the output audio file path
extract_audio(video_filepath, audio_filepath)
