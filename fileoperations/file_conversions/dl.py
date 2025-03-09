from pytube import Playlist

playlist = Playlist(
    "https://www.youtube.com/playlist?list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf"
)
print("Number of videos in playlist: %s" % len(playlist.video_urls))
playlist.download_all()
