from argparse import ArgumentParser, Namespace
from pathlib import Path
import platform

with open('version.txt', 'r') as f:
    file = f.readlines()[0]

parser = ArgumentParser()
parser.add_argument('-v', '--version', action="version", version=f"Version: {file}, Platform: {platform.system()} {platform.release()} {platform.architecture()[0]} {platform.processor()}")
parser.add_argument('path')
parser.add_argument('output')

args: Namespace = parser.parse_args()

inputdir = Path(args.path)
outputdir = Path(args.output)

if not inputdir.exists():
    print("The input directory doesn't exist!")
    raise SystemExit(1)

if not outputdir.exists():
    print("The output directory doesn't exist!")
    raise SystemExit(1)

print(f'Path is: {inputdir}\nOutput is: {outputdir}')