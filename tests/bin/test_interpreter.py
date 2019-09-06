from unittest import TestCase

from bin.interpreter import build_arg_parser


class TestInterpreterArgs(TestCase):
    def setUp(self) -> None:
        self.args = build_arg_parser()

    def test_empty_args(self):
        args = self.args.parse_args([])
        self.assertIsNone(args.filename)

    def test_filename_args(self):
        filename = 'filename.ext'

        args = self.args.parse_args([filename])
        self.assertEqual(filename, args.filename)
