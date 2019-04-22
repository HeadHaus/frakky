class File:
    name = None
    full_path = None

    def __init__(self, name, full_path):
        self.name = name
        self.full_path = full_path

    def get_full_path(self):
        full_path = self.full_path.replace("\\", "/")
        return full_path

    def __str__(self):
        return self.name + '\n'
