"""Parser for the math game bot."""


class Parser:
    """Parser class for the math game."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current_index = 0
