from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("prnumber",
                    nargs=1,
                    help="Pull request number",
                    type=int)
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")


def init_args():
    return parser.parse_args()
