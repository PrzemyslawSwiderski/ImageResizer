import glob
import ntpath
import os

from PIL import Image

from src.helpers import load_config, ensure_dir


class ImageResizer:
    def __init__(self):
        self.images_input_path = "./images_to_resize"
        self.images_output_path = "./resized_images"
        self.quality = 75
        self.extensions = ("*.jpg", "*.jpeg")
        self.input_files = []
        self.scale = 1.0
        load_config(self)

    """
    Method returns list of image files grabbed by specified extensions
    """

    def get_images_file_names(self, path):
        files_grabbed = []
        for extension in self.extensions:
            files_grabbed.extend(glob.glob(path + os.sep + "*." + extension))
        return files_grabbed

    def compress_all_files(self):
        input_files = self.get_images_file_names(self.images_input_path)
        for file in input_files:
            self.compress(file)

    def compress(self, file_name):
        old_size = os.stat(file_name).st_size
        picture = Image.open(file_name)

        file_path = self.images_output_path + os.sep + ntpath.basename(file_name)

        ensure_dir(file_path)
        new_scale = (int(picture.size[0] * self.scale), int(picture.size[1] * self.scale))
        picture = picture.resize(new_scale, Image.ANTIALIAS)
        picture.save(file_path, optimize=True, quality=self.quality)

        new_size = os.stat(file_path).st_size
        percent = (old_size - new_size) / float(old_size) * 100
        print(f"File {file_name} size changed from {old_size} to {new_size} by {percent}%")
