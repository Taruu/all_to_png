from all_to_png.file import FileObj
from all_to_png.converters import ToPngConvertor
import requests

with open("1.tif","rb") as file:
    file_bytes = file.read()
file_obj = FileObj(file_bytes)
videoC = ToPngConvertor()
file = videoC.convert(file_obj)
print(file.virtual_path)
input()
#img = requests.get('https://danbooru.donmai.us/data/21695ed9b34fb1a53fa2448efba05e01.gif')
#file_obj = FileObj(img.content)
# with open("1.mp4","rb") as file:
#     file_bytes = file.read()
# file_obj = FileObj(file_bytes)
# videoC = ToPngConvertor()
# print(file_obj.virtual_path)
# file = videoC.video_to_pngs(file_obj)
# file.generate_list_files()
# for item in file.list_virtual_files:
#     print(item.virtual_path)
#     item.get_bytes()
#     print()
# print(file.close())