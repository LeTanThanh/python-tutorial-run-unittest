import sys

import os

file_path = __file__
paths = file_path.split("/")
paths.pop() # remove __init__.py
paths.pop() # remove tests

ROOT_PATH = "/".join(paths)
SHAPES_PATH = f"{ROOT_PATH}/shapes"

sys.path.append(SHAPES_PATH)
