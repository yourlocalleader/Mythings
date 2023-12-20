import wget
import pytube
from pytube import YouTube



url = input("digite o link: ")

arquivo = input("digite o nome do arquivo: ")

wget.download(url= url, out= arquivo)








