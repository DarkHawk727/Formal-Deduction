from typing import List
from language import Language


def lexer(input_string: str) -> List[str]:
    language: Language = Language()
    tokens: List[Language] = []
    i: int = 0
    while i < len(input_string):
        if input_string[i] == " ":
            i += 1
            continue
        elif input_string[i] in Language():
            tokens.append(input_string[i])
            i += 1
        else:
            match_found: bool = False
            for op_regex in language.multi_char_operators:
                match = op_regex.match(input_string, i)
                if match:
                    token = match.group()
                    if token in language:
                        tokens.append(token)
                        i += len(token)
                        match_found = True
                        break

            if not match_found:
                raise ValueError(f"Invalid token at position {i}: '{input_string[i]}'")

    return tokens
