import os
from pathlib import Path

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path_in):
        # print('all_paths: ', self.source,self.dest, path_in)

        # print(os.path.dirname(path_in))
        # rel_path = self.dest.relative_to(self.source)
        # print('rel_path: ', rel_path)
        directory = str(self.dest) + '\\' +  str(path_in)
        # print(directory)
        # exit()
        Path(directory).mkdir(parents=True, exist_ok=True)

        # print(f"Directory {directory} created")
        # exit()

    def build(self):
        # Path(self.dest).mkdir(parents=True, exist_ok=True)
        # print(f"Directory {self.dest} created")
        # print(self.source, self.dest)
        # print(os.getcwd())
        # print(Path("content\contact.rst").relative_to("content"))

        for i in self.source.rglob("*"):
            path_dir = os.path.dirname(self.source)
            # rel_path = i.relative_to(path_dir)
            rel_path = i.relative_to(self.source)
            # print(f'dhuhkf source: {self.source}, path_dir: {path_dir}, rel_path: {rel_path}, i: {i}')
            # exit()

            if i.is_dir():
                # print('in loop: ', i, rel_path)
                self.create_dir(rel_path)

# site = Site('/pathsource/a/c', '/pathsource/a')
# site = Site("c:/Users/smid/Downloads", "c:/Users/smid/focus")
# site = Site("c:/Users/smid/focus", "c:/Users/smid/focus_cp")
# site = Site("/Downloads", "/focus")
# site.create_dir("c:/Users/smid/")
# site.build()