from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('-v', '--version', action="store_true")


args: Namespace = parser.parse_args()

if args.version:
    print('Version is: 1.0.0')