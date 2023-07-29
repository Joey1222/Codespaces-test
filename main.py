from argparse import ArgumentParser, Namespace
from pathlib import Path
import platform

class InvaildFilePathError(Exception):
    def __init__(self, pathtype):
        self.pathtype = str(pathtype)
        print(f'The {self.pathtype} file doesn\'t exist!')

with open('version.txt', 'r', encoding="utf-8") as f:
    file = f.readlines()[0]

parser = ArgumentParser()
parser.add_argument('--version', '-v', action="version", version=f"Version: {file}, Platform: {platform.system()} {platform.release()} {platform.architecture()[0]} {platform.processor()}", help="Shows version and exits")
parser.add_argument('path')
parser.add_argument('output')

args: Namespace = parser.parse_args()

inputdir = Path(args.path)
outputdir = Path(args.output)

if not inputdir.exists():
    raise InvaildFilePathError('input')

if not outputdir.exists():
    raise InvaildFilePathError('output')

print(f'Path is: {inputdir}\nOutput is: {outputdir}')