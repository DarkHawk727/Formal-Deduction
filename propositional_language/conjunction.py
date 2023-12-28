from typing import Dict, Set
from formula import Formula


class Conjunction(Formula):
    _symbol: str = "∧"

    def evaluate(self, val: Dict[str, bool]) -> bool:
        return self.left.evaluate(val=val) and self.right.evaluate(val=val)
