import sys
from cx_Freeze import setup, Executable



setup(
    name = "Python Game Base",
    version = "3.1",
    description = "A pieca shit.",
    executables = [Executable("main.py", base = "Win32GUI", compress = True, appendScriptToExe = True, appendScriptToLibrary = False)]
    )
