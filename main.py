from argparse import ArgumentParser, Namespace
from pathlib import Path

parser = ArgumentParser()
parser.add_argument('-v', '--version', action="version", version="1.0.0")
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