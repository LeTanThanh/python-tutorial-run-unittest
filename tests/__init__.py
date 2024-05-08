import sys

import os

file_path = __file__
paths = file_path.split("/")
paths.pop() # remove __init__.py
paths.pop() # remove tests

ROOT_PATH = "/".join(paths)

sys.path.append(ROOT_PATH)
