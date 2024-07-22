# This script reads a list of Mixcloud URLs from a file named 'mixcloud-to-dl.txt' and downloads each URL one at a time.
# The downloaded files are saved  to the specified download directory.
# It uses the 'yt_dlp' library to handle the downloading and conversion of audio files.

import os
import yt_dlp

def download_mixcloud(url, download_dir):
    """
    Downloads an audio track from Mixcloud and saves it as an MP3 file in the specified directory.

    Args:
        url (str): The URL of the Mixcloud track.
        download_dir (str): The directory where the MP3 file will be saved.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'ffmpeg'  # Ensure yt-dlp knows where ffmpeg is
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_from_file(filename, download_dir):
    """
    Reads Mixcloud URLs from a file and downloads each one.

    Args:
        filename (str): The name of the file containing the list of URLs.
        download_dir (str): The directory where the MP3 files will be saved.
    """
    with open(filename, 'r') as file:
        urls = file.readlines()
    for url in urls:
        url = url.strip()
        if url:
            print(f"Downloading {url}")
            download_mixcloud(url, download_dir)
            print(f"Finished downloading {url}")

if __name__ == "__main__":
    input_filename = 'mixcloud-to-dl.txt'
    download_directory = 'downloads'  # Specify the directory where you want to save the files
    os.makedirs(download_directory, exist_ok=True)  # Create the directory if it doesn't exist
    download_from_file(input_filename, download_directory)
