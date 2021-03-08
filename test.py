import ffmpeg
from PIL import Image
import io
import time
import requests
import tempfile

time_v = time.time()

img = requests.get('https://danbooru.donmai.us/data/21695ed9b34fb1a53fa2448efba05e01.gif')
print()
fp = tempfile.NamedTemporaryFile(delete=False)
fp.write(img.content)
fp.seek(0)
probe = ffmpeg.probe(fp.name)
fp.close()
print(fp.name)

data_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
print(data_stream)
width = int(data_stream['width'])
height = int(data_stream['height'])
print(data_stream['has_b_frames'])
print(time.time()-time_v)