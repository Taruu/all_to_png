import ffmpeg
import tempfile

from .file import FileObj
class VideoConverter:
    def video_to_images(self, file : FileObj, tmp_format = "png"):
        print(file.info)
        temp_dir = tempfile.TemporaryDirectory(prefix="virtual_images")
        if not file.info["codec_type"] == 'video':
            raise Exception.TypeError
        ffmpeg.input(file.virtual_path).output(temp_dir.name + '/test-%d.'+ tmp_format,
                start_number=0).overwrite_output().run()

        input()
        temp_dir.cleanup()

        #run(quiet=True)

