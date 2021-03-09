import ffmpeg
import ffmpeg
from PIL import Image
import io
import time
import os
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

class VideoFilesPng:
    def __init__(self):
        self.virtual_dir = tempfile.TemporaryDirectory(prefix="virtual_directory_")
        self.virtual_path = self.virtual_dir.name
        self.list_virtual_files = None


    def generate_list_files(self):
        self.list_virtual_files = [ImageFilePNG(path_to_file=self.virtual_path+"/"+file) for file in os.listdir(self.virtual_path)]

    def __len__(self):
        if not self.list_virtual_files:
            self.generate_list_files()
        return len(self.list_virtual_files)
        pass

    def __iter__(self):
        if not self.list_virtual_files:
            self.generate_list_files()
        return self.list_virtual_files

    def __getitem__(self, key):
        if not self.list_virtual_files:
            self.generate_list_files()
        return self.list_virtual_files[key]

    def __del__(self):
        self.virtual_dir.cleanup()

    def close(self):
        self.virtual_dir.cleanup()

class ImageFilePNG:
    def __init__(self, bytes_in=None, path_to_file=None):
        self.virtual_file = tempfile.NamedTemporaryFile(suffix="_virtual_image.png")

        if path_to_file:
            if not os.path.isfile(path_to_file):
                raise Exception.FileNotFound
            self.virtual_path = path_to_file
            self.bytes = None
        if bytes_in:
            self.virtual_file.write(bytes_in)
            self.virtual_file.seek(0)
            self.bytes = bytes_in
            self.virtual_path = self.virtual_file.name
        else:
            self.virtual_path = self.virtual_file.name

    def __bytes__(self):
        if not self.bytes:
            with open(self.virtual_path, "rb") as file:
                self.bytes = file.read()
        return self.bytes

    def __del__(self):
        self.virtual_file.close()

    def close(self):
        self.virtual_file.close()


