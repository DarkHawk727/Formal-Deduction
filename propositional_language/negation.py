from typing import Any, Dict, Set, Tuple
from formula import Formula


class Negation(Formula):
    def __init__(self, right: Formula) -> None:
        self.right = right

    def __str__(self) -> str:
        return f"(¬{self.right})"

    def __key(self):
        return (self.right,)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Negation):
            return self.__key() == other.__key()
        raise NotImplementedError

    def evaluate(self, val: Dict[str, bool]) -> bool:
        return not self.right.evaluate(val=val)

    def variables(self) -> Set[str]:
        return self.right.variables()
