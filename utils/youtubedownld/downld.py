from pytube import YouTube

YouTube("https://www.youtube.com/watch?v=s7NgczFZsII").streams.first().download()
#ask for the link from user
link = input("https://www.youtube.com/watch?v=BGdZw1aGIdw")
yt = YouTube(link)
#
# #Showing details
# print("Title: ",yt.title)
# print("Number of views: ",yt.views)
# print("Length of video: ",yt.length)
# print("Rating of video: ",yt.rating)
# #Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()
#
# #Starting download
# print("Downloading...")
ys.download()
print("Download completed!!")