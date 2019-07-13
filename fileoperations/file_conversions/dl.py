from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?list=PLMeIm5cDxqlMxcBC9CnS5Sm3VhZ6yYCoa')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()