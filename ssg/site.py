from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        # print('all_paths: ', self.source,self.dest, path_in)

        # print(os.path.dirname(path_in))
        # rel_path = self.dest.relative_to(self.source)
        # print('rel_path: ', rel_path)
        # directory = str(self.dest) + '\\' +  str(path)

        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

        # print(directory)
        # exit()
        # Path(directory).mkdir(parents=True, exist_ok=True)

        # print(f"Directory {directory} created")
        # exit()

    def build(self):
        # Path(self.dest).mkdir(parents=True, exist_ok=True)
        # print(f"Directory {self.dest} created")
        # print(self.source, self.dest)
        # print(os.getcwd())
        # print(Path("content\contact.rst").relative_to("content"))

        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)