from pathlib import Path
import typer
from ssg.site import Site
import os

def main(source = "content", dest = "dist"):
    # path = os.getcwd()
    # if 'config' not in path:
    #     # print(str(path) + '\\config')
    #     Path(str(path) + '\\config').mkdir(parents=True, exist_ok=True)

    config = {"source": source, "dest": dest}

    site = Site(**config).build()

typer.run(main)
