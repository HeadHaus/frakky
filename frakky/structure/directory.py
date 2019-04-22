class Directory:

    name = None
    full_path = None

    def __init__(self, name, full_path):
        self.name = name
        self.full_path = full_path

        self.subdirectories = []
        self.files = []
        self.all_files = []

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)

    def add_file(self, file):
        self.files.append(file)

    def find_all_files(self):
        self.all_files = []
        for subdirectory in self.subdirectories:
            subdirectory.find_all_files()
        self.all_files.extend(self.files)
        for subdirectory in self.subdirectories:
            self.all_files.extend(subdirectory.all_files)

    def __str__(self):
        s = self.name + '\n'
        for file in self.files:
            s += str(file)
        for subdirectory in self.subdirectories:
            s += str(subdirectory)
        return s
