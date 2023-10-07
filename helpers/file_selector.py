import tkinter as tk
from tkinter import filedialog

class FileSelector:
    def select_file(self):
        file_path = filedialog.askopenfilename()
        return file_path
