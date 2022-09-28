from pytube import Playlist

# input to get Url from user
playlist_url = input('Please enter your Playlist: ')

p = Playlist(playlist_url)

print(f'Downloading: {p.title}')

#looping in each video playlist
for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()