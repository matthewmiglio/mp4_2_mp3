@echo off
cd /d c:\My_Files\my_programs\mp4_2_mp3
title mp4_to_mp3
poetry install --no-root
poetry run python mp4_to_mp3.py
pause