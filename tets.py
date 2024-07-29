import pathlib
import sys

print(sys.path[0])
print(pathlib.Path(__file__).parents[2].resolve().as_posix())

sys.path.insert(0, pathlib.Path(__file__).parent.resolve().as_posix())

print(__file__)