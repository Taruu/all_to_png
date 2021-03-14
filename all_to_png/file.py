import ffmpeg
import ffmpeg
from PIL import Image
import io
import time
import os
import requests
import tempfile

class FileObj:
    """Object for identification. Receives bytes"""
    def __init__(self, bytes_in : bytes):
        self.virtual_file = tempfile.NamedTemporaryFile(prefix="_virtual_image")
        self.virtual_file.write(bytes_in)
        self.virtual_file.seek(0)
        self.virtual_path = self.virtual_file.name
        try:
            probe = ffmpeg.probe(self.virtual_path)
            data_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            if data_stream.get("nb_frames"):
                data_stream["codec_type"] = "video"
            else:
                data_stream["codec_type"] = "image"
            self.info = data_stream
        except:
            self.info = None

    def __del__(self):
        self.virtual_file.close()

    def close(self):
        self.virtual_file.close()

class VideoFilesPng:
    """Video Object"""
    def __init__(self):
        self.virtual_dir = tempfile.TemporaryDirectory(prefix="virtual_directory_")
        self.virtual_path = self.virtual_dir.name
        self.list_virtual_files = None

    def generate_list_files(self):
        self.list_virtual_files = [ImageFilePNG(path_to_file=self.virtual_path+"/"+file) for file in os.listdir(self.virtual_path)]
        return self.list_virtual_files

    def __del__(self):
        self.virtual_dir.cleanup()

    def close(self):
        self.virtual_dir.cleanup()

class ImageFilePNG:
    """Image object"""
    def __init__(self, bytes_in=None, path_to_file=None, tmp_format = "png"):

        self.virtual_file = tempfile.NamedTemporaryFile(suffix="_virtual_image." + tmp_format)
        if path_to_file:
            if not os.path.isfile(path_to_file):
                raise Exception.FileNotFound
            self.virtual_path = path_to_file
            self.bytes = None
        elif bytes_in:
            self.virtual_file.write(bytes_in)
            self.virtual_file.seek(0)
            self.bytes = bytes_in
            self.virtual_path = self.virtual_file.name
        else:
            self.virtual_path = self.virtual_file.name


    def get_bytes(self):
        with open(self.virtual_path, "rb") as file:
            self.bytes = file.read()
        return self.bytes

    def __del__(self):
        self.virtual_file.close()

    def close(self):
        self.virtual_file.close()


