from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk, filedialog
import customtkinter
from googleapiclient.discovery import build
from pytube import YouTube
import webbrowser
import os

api_key = 'AIzaSyBith2ceOhkC7QOchCUZizC7xO7RGh5Qxg'
youtube = build('youtube', 'v3', developerKey=api_key)

def download_video(video_url, download_path):
    # Create a YouTube object
    yt = YouTube(video_url)
    # Get the highest resolution video stream
    video_stream = yt.streams.get_highest_resolution()
    # Download the video
    video_stream.download(download_path)
    return (yt.author, yt.title)

def time_to_seconds(time_str):
    hours, minutes, seconds_with_ms = map(str, time_str.split(':'))
    seconds, milliseconds = map(int, seconds_with_ms.split(','))
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + milliseconds / 1000.0

def open_sk():
    url = 'https://www.karaoketexty.cz/' # Change this URL to the desired website
    webbrowser.open_new(url)

def open_en():
    url = 'https://www.rentanadviser.com/subtitles/subtitles4songs.aspx' # Change this URL to the desired website
    webbrowser.open_new(url)


def generate_srt(sk, english_subtitles_path):
    en = open(english_subtitles_path, 'r', encoding='utf-8')
    en = en.readlines()

    line_counter_slovak = 0
    line_counter = 0
    subtitles = []
    lyrics = ''
    time = (0,0)

    for line in en:
        line = line.encode('utf-8').decode('utf-8-sig')
        stripped = (line.strip())

        if stripped == '':
            line_counter += 1
            line_counter_slovak = 0
            subtitles.append((time, lyrics))
            lyrics = ''

        else:
            str_line = str(line_counter)
            if str_line == stripped:
                continue
            elif "-->" in line and line_counter_slovak == 0:
                times = line.split()
                time = (time_to_seconds(times[0]), time_to_seconds(times[2]))
            elif stripped[0].isalpha() and line_counter_slovak == 0:
                lyrics += sk[line_counter]
                line_counter_slovak +=1
            else:
                line_counter_slovak = 0

    return subtitles


def add_subtitles(url, sk_srt, en_srt, dir_path):
    video_info = download_video(url, '')
    video_name = video_info[1] + '.mp4'

    output_name = dir_path + '/' + video_info[0] + '-' + video_name

    subs = generate_srt(sk_srt, en_srt)

    # Load the video clip
    main_video = VideoFileClip(video_name)
    generator = lambda txt: TextClip(txt, font="Georgia-Regular", fontsize=30, color="white", bg_color = 'black', method='caption', align='south', size=main_video.size).set_pos(('center', 'bottom'))

    # Create SubtitlesClip from the loaded subtitle list
    sub_clip = SubtitlesClip(subs, generator)

    # Composite the video clip with subtitles
    result = CompositeVideoClip([main_video, sub_clip.set_pos(('center', 'bottom'))], size=main_video.size)

    # Write the result to a file
    result.write_videofile(output_name, fps=24, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", threads = 16)

    os.remove(video_name)

def create_subtitles(sk_srt, en_srt, dir_path):
    file_name = os.path.basename(en_srt)

    output_video_name = dir_path + '/' + file_name 
    en = open(en_srt, 'r', encoding='utf-8')
    en = en.readlines()

    new_sk = open(output_video_name, 'w', encoding='utf-8')

    line_counter_slovak = 0
    line_counter = 0
  
    for line in en:
        line = line.encode('utf-8').decode('utf-8-sig')
        stripped = (line.strip())

        if stripped == '':
            new_sk.write('\n')
            new_sk.write('\n')
            line_counter += 1
            line_counter_slovak = 0


        else:
            str_line = str(line_counter)
            if str_line == stripped:
                new_sk.write(line)
            elif "-->" in line and line_counter_slovak == 0:
                new_sk.write(line)
            elif stripped[0].isalpha() and line_counter_slovak == 0:
                new_sk.write(sk_srt[line_counter])
                line_counter_slovak +=1
            else:
                line_counter_slovak = 0

    new_sk.close()

"""
if __name__ == "__main__":

    sk_srt = "video/text.txt"
    en_srt = "video/lakes.srt"
    url = 'https://www.youtube.com/watch?v=tOHcAc3r2kw'

    add_subtitles(url, sk_srt, en_srt)
"""


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
    en_srt_entry.delete(0, tk.END)
    en_srt_entry.insert(0, filename)

def browse_save_path():
    save_path = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(0, save_path)


def button():
    dir_path = save_path_entry.get()
    url = url_entry.get()
    sk_srt = sk_srt_text.get("1.0", tk.END).strip()
    en_srt = en_srt_entry.get()

    sk_lines = sk_srt.splitlines()
    sk = [line for line in sk_lines if line.strip() != '']

    if url and sk_srt and en_srt and dir_path:
        result_label.configure(text="Pracuje sa na tom!")
        add_subtitles(url, sk, en_srt, dir_path)
        result_label.configure(text="Pridane titulky!")
    else:
        result_label.configure(text="Vypln vsetky policka.")

def titulky_button():
    dir_path = save_path_entry.get()
    url = url_entry.get()
    sk_srt = sk_srt_text.get("1.0", tk.END).strip()
    en_srt = en_srt_entry.get()

    sk_lines = sk_srt.splitlines()
    sk = [line for line in sk_lines if line.strip() != '']

    if sk_srt and en_srt and dir_path:
        create_subtitles(sk, en_srt, dir_path)
        result_label.configure(text="Vytvorene titulky!")
    else:
        result_label.configure(text="Vypln vsetky policka.")

def download_video_button():
    dir_path = save_path_entry.get()
    url = url_entry.get()

    if url and dir_path:
        download_video(url, dir_path)
        result_label.configure(text="Stiahnute video!")
    else:
        result_label.configure(text="Vypln vsetky potrebne policka.")

def clear_text_fields():
    url_entry.delete(0, tk.END)
    en_srt_entry.delete(0, tk.END)
    sk_srt_text.delete("1.0", tk.END)
    save_path_entry.delete(0, tk.END)


customtkinter.set_appearance_mode("dark")
# Create the main window
app = customtkinter.CTk()
app.title("Subtitles App")
app.geometry("1200x500")  

# Create and place widgets
url_label = customtkinter.CTkLabel(app, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
url_entry = customtkinter.CTkEntry(app, width=500)
url_entry.grid(row=0, column=1, columnspan=1, pady=5)

en_srt_label = customtkinter.CTkLabel(app, text="Anglicke titulky:")
en_srt_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
en_srt_entry = customtkinter.CTkEntry(app, width=500)
en_srt_entry.grid(row=1, column=1, pady=5)
browse_button = customtkinter.CTkButton(app, text="Vybrat", command=browse_file)
browse_button.grid(row=1, column=2, pady=10, padx=20)
open_website_button = customtkinter.CTkButton(app, text="Najst na Stranke", command=open_en)
open_website_button.grid(row=1, column=3, pady=10, padx=20)

sk_srt_label = customtkinter.CTkLabel(app, text="Slovenske Titulky:")
sk_srt_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
sk_srt_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=10)
sk_srt_text.grid(row=2, column=1, pady=5)
open_website_button = customtkinter.CTkButton(app, text="Najst na Stranke", command=open_sk)
open_website_button.grid(row=2, column=2, pady=10)


# Create and place widgets for save path
save_path_label =customtkinter.CTkLabel(app, text="Ulozit video: ")
save_path_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
save_path_entry = customtkinter.CTkEntry(app, width=500)
save_path_entry.grid(row=3, column=1, pady=5)
browse_save_path_button = customtkinter.CTkButton(app, text="Vybrat", command=browse_save_path)
browse_save_path_button.grid(row=3, column=2, pady=5)

preloz_button = customtkinter.CTkButton(app, text="Prelozit", command=button)
preloz_button.grid(row=4, column=1, pady=10)

titulky_button = customtkinter.CTkButton(app, text="Vytvor titulky", command=titulky_button)
titulky_button.grid(row=4, column=0, pady=10, padx = 20)


video_button = customtkinter.CTkButton(app, text="Stiahnut video", command=download_video_button)
video_button.grid(row=4, column=2, pady=10)

clear_button = customtkinter.CTkButton(app, text="Vycistit policka", command=clear_text_fields)
clear_button.grid(row=4, column=3, pady=10, padx=10)

result_label = customtkinter.CTkLabel(app, text="")
result_label.grid(row=5, column=0, columnspan=3, pady=5)

# Start the Tkinter event loop
app.mainloop()
