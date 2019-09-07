from typing import List, Optional

from proglang.token import Token, TokenType


def is_digit(c: str) -> bool:
    return '0' <= c <= '9'


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.current = 0

    def scan_tokens(self) -> List[Token]:
        tokens = []

        while not self._is_at_end():
            self.start = self.current
            token = self.scan_token()
            if token is None:
                continue
            tokens.append(token)

        tokens.append(Token(TokenType.EOF, '', None))

        return tokens

    def scan_token(self) -> Optional[Token]:
        c = self._advance()

        if c == '+':
            return self._add_token(TokenType.PLUS_OPERATOR)
        elif c == '-':
            return self._add_token(TokenType.MINUS_OPERATOR)
        elif c == '*':
            return self._add_token(TokenType.MULTIPLY_OPERATOR)

        elif c == ' ' or c == '\r' or c == '\t':
            return None
        elif c == '\n':
            # TODO(alexander-lloyd): Include line numbers in Tokens.
            pass

        elif is_digit(c):
            return self._number()

        else:
            # Error
            pass

    def _is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def _advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    def _peek(self) -> str:
        if self._is_at_end():
            return '\0'
        return self.source[self.current]

    def _peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def _add_token(self, token_type: TokenType, literal: object = None) -> Token:
        text = self.source[self.start:self.current]

        return Token(token_type, text, literal)

    def _number(self) -> Token:
        while is_digit(self._peek()):
            self._advance()

        if self._peek() == '.' and is_digit(self._peek_next()):
            # Consume .
            self._advance()

            while is_digit(self._peek()):
                self._advance()

        return self._add_token(
            TokenType.NUMBER,
            float(self.source[self.start:self.current])
        )
