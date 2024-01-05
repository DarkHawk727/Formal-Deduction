from typing import Dict, Set
from formula import Formula


class Implication(Formula):
    _symbol: str = "→"

    def evaluate(self, val: Dict[str, bool]) -> bool:
        if isinstance(self.left, Formula) and isinstance(self.right, Formula):
            return not self.left.evaluate(val=val) or self.right.evaluate(val=val)
        raise NotImplementedError
