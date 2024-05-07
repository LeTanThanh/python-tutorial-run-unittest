import os

file_path = __file__
paths = file_path.split("/")
paths.pop() # remove path
paths.pop() # remove test

ROOT_PATH = "/".join(paths)
SHAPES_PATH = f"{ROOT_PATH}/shapes"
