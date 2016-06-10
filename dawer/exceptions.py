class NotValidPath(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return '"{path}" is not a valid Path.'.format(
            path=self.path
        )
