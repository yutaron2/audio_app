from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "tkinter", "moviepy"],
    "excludes": ["pygame"],  # Exclude unnecessary packages
}

setup(
    name="AudioExtractorApp",
    version="0.1",
    description="An application to extract audio from video",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)
