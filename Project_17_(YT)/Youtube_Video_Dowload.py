import yt_dlp
import os
import time
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        opt = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': f"{save_path}/%(resolution)s_%(title)s.%(ext)s",
            'ffmpeg_location': r"C:\Users\sriva\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
            'merge_output_format': 'mp4'
        }
        
        with yt_dlp.YoutubeDL(opt) as ydl:
            info = ydl.extract_info(url, download = False)
            
        # Get the output filename
        downloaded_filename = ydl.prepare_filename(info)
        
        if os.path.exists(downloaded_filename):
            print(f"File Already Exist: {downloaded_filename}.")
        else:
            ydl.download([url])
            # Update the file's modified date to the current time
            current_time = time.time()
            os.utime(downloaded_filename, (current_time, current_time))
            print("Downloaded Successfully!!!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def open_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(F'Select Folder: "{folder}".')
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    url = input("Enter the YouTube video URL: ")
    path = open_dialog()

    if path:
        download_video(url, path)
    else:
        print("Invalid Save Location...")

#https://youtu.be/jNQXAC9IVRw
