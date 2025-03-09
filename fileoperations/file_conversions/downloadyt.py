import pytube

f = open("links_file.txt", "r")
text = f.read()
links = text.splitlines()
for link in links:
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()
f.close()
