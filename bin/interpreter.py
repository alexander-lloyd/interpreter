import argparse
import logging

from proglang import Scanner

logger = logging.getLogger(__name__)


def build_arg_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', metavar='filename', nargs='?', default=None)

    return parser


def run_repl():
    try:
        while True:
            line = input('>>> ')
            logger.debug(line)
            scanner = Scanner(line)
            tokens = scanner.scan_tokens()
            print(tokens)
    except KeyboardInterrupt:
        pass


def run_file(source_file):
    pass


def main():
    argparser = build_arg_parser()
    args = argparser.parse_args()

    source_file = args.filename

    if source_file is None:
        # REPL
        run_repl()
    else:
        code = open(source_file)
        run_file(code)


if __name__ == '__main__':
    main()
