''' require import this module '''

from typing import List
from pathlib import Path
import shutil


class Parser:
    ''' extensions is type of List[str] '''
    extensions : List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        ''' All inputs has to be a Path type '''
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r', encoding='UTF-8') as file:
            # print(file.read())
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name

        with open(full_path, 'w', encoding='UTF-8') as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))

# parser = Parser()
# ext = parser.valid_extension('ex')
# print(ext)
# parser.parse(Path('sdsdsds'),Path('sdsdsaa'),Path('xxxxxdsds'))
# p = parser.read('textFile')
# print(p)
# print(Path('filename').with_suffix('.ext'))
# print(Path('filename') / Path('kolo/asap').with_suffix('.ext').name, Path('filename2') / Path('kolo/asap').with_suffix('.ext'), sep='\n')

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)