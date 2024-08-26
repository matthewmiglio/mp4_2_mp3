import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip


class VideoToAudioConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video to Audio Converter")

        self.source_folder_var = tk.StringVar()
        self.destination_folder_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select Source Folder:").grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Entry(
            self.master, textvariable=self.source_folder_var, width=40, state="disabled"
        ).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.master, text="Browse", command=self.browse_source_folder).grid(
            row=0, column=2, padx=5, pady=5
        )

        tk.Label(self.master, text="Select Destination Folder:").grid(
            row=1, column=0, padx=5, pady=5
        )
        tk.Entry(
            self.master,
            textvariable=self.destination_folder_var,
            width=40,
            state="disabled",
        ).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(
            self.master, text="Browse", command=self.browse_destination_folder
        ).grid(row=1, column=2, padx=5, pady=5)

        tk.Button(self.master, text="GO!", command=self.start_conversion).grid(
            row=2, column=1, pady=10
        )

        self.progress_label = tk.Label(self.master, text="")
        self.progress_label.grid(row=3, column=0, columnspan=3, pady=10)

    def browse_source_folder(self):
        folder_path = filedialog.askdirectory()
        self.source_folder_var.set(folder_path)

    def browse_destination_folder(self):
        folder_path = filedialog.askdirectory()
        self.destination_folder_var.set(folder_path)

    def start_conversion(self):
        source_folder = self.source_folder_var.get()
        destination_folder = self.destination_folder_var.get()

        if source_folder and destination_folder:
            self.convert_videos(source_folder, destination_folder)
        else:
            self.progress_label.config(
                text="Please select both source and destination folders."
            )

    def convert_videos(self, source_folder, destination_folder):
        os.makedirs(destination_folder, exist_ok=True)

        for file_name in os.listdir(source_folder):
            if file_name.endswith(".mp4"):
                input_path = os.path.join(source_folder, file_name)
                self.convert_to_mp3(input_path, destination_folder)

    def convert_to_mp3(self, input_path, output_path, bitrate="192k"):
        try:
            video_clip = VideoFileClip(input_path)
            audio_clip = video_clip.audio
            output_file = os.path.join(
                output_path, os.path.splitext(os.path.basename(input_path))[0] + ".mp3"
            )
            audio_clip.write_audiofile(output_file, bitrate=bitrate)
            print(f"Conversion successful: {output_file}")
            self.progress_label.config(text=f"Conversion successful: {output_file}")
        except Exception as e:
            print(f"Error converting {input_path}: {e}")
            self.progress_label.config(text=f"Error converting {input_path}: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToAudioConverterApp(root)
    root.mainloop()
