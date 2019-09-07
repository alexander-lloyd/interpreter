from unittest import TestCase

from proglang import Scanner, TokenType, Token

cases = [
    ['1', [Token(TokenType.NUMBER, '1', 1.0), Token(TokenType.EOF, '', None)]],
    ['1.', [
        Token(TokenType.NUMBER, '1', 1.0),
        Token(TokenType.EOF, '', None)
    ]],
    ['123', [Token(TokenType.NUMBER, '123', 123.0), Token(TokenType.EOF, '', None)]],
    ['123.45', [Token(TokenType.NUMBER, '123.45', 123.45), Token(TokenType.EOF, '', None)]],
    ['1+2', [
        Token(TokenType.NUMBER, '1', 1.0),
        Token(TokenType.PLUS_OPERATOR, '+', None),
        Token(TokenType.NUMBER, '2', 2.0),
        Token(TokenType.EOF, '', None)
    ]],
    ['1-1', [
        Token(TokenType.NUMBER, '1', 1.0),
        Token(TokenType.MINUS_OPERATOR, '-', None),
        Token(TokenType.NUMBER, '1', 1.0),
        Token(TokenType.EOF, '', None)
    ]],
    ['5*5', [
        Token(TokenType.NUMBER, '5', 5.0),
        Token(TokenType.MULTIPLY_OPERATOR, '*', None),
        Token(TokenType.NUMBER, '5', 5.0),
        Token(TokenType.EOF, '', None)
    ]],
    ['25   +  12', [
        Token(TokenType.NUMBER, '25', 25.0),
        Token(TokenType.PLUS_OPERATOR, '+', None),
        Token(TokenType.NUMBER, '12', 12.0),
        Token(TokenType.EOF, '', None)
    ]],
    ['\n', [
        Token(TokenType.EOF, '', None)
    ]]
]


class TestScanner(TestCase):
    def test_scanner(self):
        for (source, tokens) in cases:
            with self.subTest('Input {}'.format(source)):
                scanner = Scanner(source)
                expected_tokens = scanner.scan_tokens()
                self.assertEqual(tokens, expected_tokens)
