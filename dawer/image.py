from .filesystem import get_images_in_folder
from .process import DateParser


class Image:
    date = None

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def extract_date_from_name(self, dateparser):
        self.date = dateparser.get_date(self.filename)


class ImagesHandler:
    images = []

    def __init__(self, destination_path=None):
        self.destination_path = destination_path
        self.dateparser = DateParser()

    def load_images_from_path(self, directory):
        filenames = get_images_in_folder(directory)
        for filename in filenames:
            image = Image(directory, filename)
            image.extract_date_from_name(self.dateparser)
            self.images.append(image)
