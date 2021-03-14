import ffmpeg
import tempfile

from .file import FileObj,VideoFilesPng,ImageFilePNG




class ToPngConvertor:

    def convert(self, file : FileObj):
        if file.info["codec_type"] == 'video':
           return self.video_to_pngs(file)
        elif file.info["codec_type"] == "image":
            return self.image_to_png(file)
        else:
            return None


    def video_to_pngs(self, file : FileObj, tmp_format = "png"):
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
        file.close()
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
            file.close()
            return None
        file.close()
        return image