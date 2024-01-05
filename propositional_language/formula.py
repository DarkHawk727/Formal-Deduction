from __future__ import annotations
from typing import Any, Dict, Optional, Set
from abc import ABC, abstractmethod


class Formula(ABC):
    _symbol: str = "X"

    def __init__(
        self, left: Optional[Formula] = None, right: Optional[Formula] = None
    ) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left_str, right_str = str(self.left), str(self.right)

        if isinstance(self.left, Formula) and self.left._symbol == self._symbol:
            left_str = left_str[1:-1]

        if isinstance(self.right, Formula) and self.right._symbol == self._symbol:
            right_str = right_str[1:-1]

        return f"({left_str} {self._symbol} {right_str})"

    def __repr__(self) -> str:
        return self.__str__()

    def __key(self):
        return (self.left, self.right)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Formula):
            return self.__key() == other.__key()
        raise NotImplementedError

    @abstractmethod
    def evaluate(self, val: Dict[str, bool]) -> bool:
        pass

    def variables(self) -> Set[str]:
        if self.left and self.right:
            return self.left.variables() | self.right.variables()
        raise NotImplementedError
