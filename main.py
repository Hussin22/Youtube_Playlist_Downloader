from pytube import Playlist

playlist_url = input('Please enter your Playlist: ')
p = Playlist(playlist_url)

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()