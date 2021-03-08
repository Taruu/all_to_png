import ffmpeg
import ffmpeg
from PIL import Image
import io
import time
import requests
import tempfile

class FileObj:
    def __init__(self, bytes):
        self.virtual_file = tempfile.NamedTemporaryFile(prefix="_virtual_image")
        self.virtual_file.write(bytes)
        self.virtual_file.seek(0)
        self.virtual_path = self.virtual_file.name
        try:
            probe = ffmpeg.probe(self.virtual_path)
            data_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            print(data_stream)
            if data_stream.get("nb_frames"):
                data_stream["codec_type"] = "video"
            else:
                data_stream["codec_type"] = "image"
            self.info = data_stream
        except:
            self.info = None

    def close(self):
        self.virtual_file.close()

class CookedFile:
