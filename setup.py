from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "tkinter", "moviepy"],
    "excludes": ["tkinter.ttk", "tkinter.tix", "tkinter.scrolledtext"],
    "include_files": ["audio_extractor.py", "youtube_downloader.py", "audio_player.py", "helpers/"]
}

base = None

setup(
    name = "MyApp",
    version = "0.1",
    description = "My Application",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)]
)
