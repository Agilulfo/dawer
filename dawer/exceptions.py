class NotValidPath(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return '"{path}" is not a valid Path.'.format(
            path=self.path
        )


class UnknownImageDate(Exception):
    def __init__(self, image):
        self.image = image

    def __str__(self):
        msg = 'Unkwnown date for image: {name}'
        return msg.format(name=self.image.filename)
