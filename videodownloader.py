from pytube import YouTube

urlvideo = input("digite o link do video: ")

YouTube(urlvideo).streams.get_highest_resolution().download()