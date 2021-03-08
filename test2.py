from all_to_png.file import FileObj
from all_to_png.converters import VideoConverter
import requests

#img = requests.get('https://danbooru.donmai.us/data/21695ed9b34fb1a53fa2448efba05e01.gif')
#file_obj = FileObj(img.content)
with open("1.mp4","rb") as file:
    file_bytes = file.read()
file_obj = FileObj(file_bytes)
videoC = VideoConverter()
print(file_obj.virtual_path)
videoC.video_to_images(file_obj)
