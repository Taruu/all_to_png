import ffmpeg
import tempfile

from .file import FileObj,VideoFilesPng,ImageFilePNG




class ToPngConvertor:
    def video_to_pngs(self, file : FileObj, tmp_format = "png"):
        print(file.info["codec_type"])
        if not file.info["codec_type"] == 'video':
            return None
        images = VideoFilesPng()
        try:
            ffmpeg \
                .input(file.virtual_path). \
                output(images.virtual_path + '/image-%d.' + tmp_format, start_number=0) \
                .overwrite_output() \
                .run(quiet=True)
        except:
            return None
        images.generate_list_files()
        return images

    def image_to_png(self, file : FileObj, tmp_format = "png"):
        if not file.info["codec_type"] == 'image':
            return None
        image = ImageFilePNG()
        try:
            ffmpeg \
                .input(file.virtual_path). \
                output(image.virtual_path, start_number=0) \
                .overwrite_output() \
                .run(quiet=True)
        except:
            return None
        return image