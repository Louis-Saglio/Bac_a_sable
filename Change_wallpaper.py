from os import system, listdir
from random import choice


path = "/home/louis/Images/Wallpapers/"
cmd = 'gsettings set org.gnome.desktop.background picture-uri "file://'

wallpaper_name = choice(listdir(path))
print(wallpaper_name)

system(cmd + path + wallpaper_name + '"')
