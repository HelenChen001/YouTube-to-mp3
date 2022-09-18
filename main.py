from email.mime import audio
from hashlib import new
from pytube import YouTube
import os 

#MUSIC_PATH = "Enter your own local path"


# Takes a youtube link and only filter the audio only.
# The user can pick which version they want.
# Downloads the file and converts the mp4 file to a mp3 file 
# Places the mp3 file into the designated folder

def download_audio(url):

    try:
        yt = YouTube(url)
        audios = yt.streams.filter(only_audio=True)
        audio = list(enumerate(audios))
        for i in audio:
            print(i)

        print("Enter a number of which you want the audio to be formatted: ")
        download_format = int(input("Enter format number: "))

        out_file = audios[download_format].download(MUSIC_PATH)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " Has been successfully downloaded.")
    
    except:
        print("Error with downloading the mp3 file")
        exit()

# Takes a link and downloads it
if __name__ == '__main__':
    print("Enter the link of the video: ")
    url = input()
    download_audio(url)