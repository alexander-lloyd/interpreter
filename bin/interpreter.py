import argparse


def build_arg_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', metavar='filename', nargs='?', default=None)

    return parser


def main(program_args):
    print("--- Interpreter ---")
    print(program_args)


if __name__ == '__main__':
    argparser = build_arg_parser()
    args = argparser.parse_args()
    main(args)
