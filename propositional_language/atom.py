from typing import Any, Dict, Set, Tuple
from formula import Formula


class Atom(Formula):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __key(self) -> Tuple[str]:
        return (self.name,)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Atom):
            return self.__key() == other.__key()
        raise NotImplementedError

    def evaluate(self, val: Dict[str, bool]) -> bool:
        return val[self.name]

    def variables(self) -> Set[str]:
        return set(self.name)
