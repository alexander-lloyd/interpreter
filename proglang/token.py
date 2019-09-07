from enum import Enum


class TokenType(Enum):
    # Operators
    PLUS_OPERATOR = 'PLUS_OPERATOR'
    MINUS_OPERATOR = 'MINUS_OPERATOR'
    MULTIPLY_OPERATOR = 'MULTIPLY_OPERATOR'
    DIVIDE_OPERATOR = 'DIVIDE_OPERATOR'

    # Number Literal
    NUMBER = 'NUMBER'

    # EOF
    EOF = 'EOF'

    def __repr__(self):
        return self.name, self.value


class Token:
    def __init__(self, token_type: TokenType, lexeme: str, literal: object):
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal

    def __repr__(self) -> str:
        return f'Token({self.token_type},{self.lexeme})>'

    def __eq__(self, other: 'Token') -> bool:
        return (
            self.token_type == other.token_type and
            self.lexeme == other.lexeme and
            self.literal == self.literal
        )
