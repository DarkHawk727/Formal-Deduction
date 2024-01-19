from re import compile
from typing import List, Pattern, Set


class Language:
    single_char_tokens: Set[str] = {"(", ")", "&", "v", "~"}
    multi_char_operators: List[Pattern[str]] = [compile(r"->"), compile(r"<->")]

    @staticmethod
    def __is_letter(char: str) -> bool:
        return char.isalpha() and len(char) == 1

    @classmethod
    def __contains__(cls, token: str) -> bool:
        if cls.__is_letter(token) or token in cls.single_char_tokens:
            return True
        for op_regex in cls.multi_char_operators:
            if op_regex.fullmatch(token):
                return True
        return False
