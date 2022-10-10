import os

from pytube import Playlist
from pytube import YouTube


def playlist(playlist_url):
    # input to get Url from user

    start_index = input('from?')

    p = Playlist(playlist_url)

    print(f'Downloading: {p.title}')
    i = int(start_index);
    #looping in each video playlist
    lenget = len(p.videos)
    print(lenget)
    for index ,video in enumerate(p.videos,start=1):
        if(index >=i ):
            print(video.title)
            st = video.streams.get_highest_resolution()
            st.download(os.getcwd()+"/"+p.title)
        else:
            pass


url = input('Please enter your video or playlist url: ')


def Video(url):
    yt =YouTube(url)
    print(yt.title)
    st = yt.streams.get_highest_resolution()
    st.download()



if ("playlist" in url):
    playlist(url)

elif("watch" in url):
    Video(url)

else:
    print("wrong url...")