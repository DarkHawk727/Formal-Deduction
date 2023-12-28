from typing import Dict, Set
from formula import Formula


class Bidirectional(Formula):
    _symbol: str = "↔"
    
    def evaluate(self, val: Dict[str, bool]) -> bool:
        return (
            not self.left.evaluate(val=val)
            or self.right.evaluate(val=val)
        ) and (
            not self.right.evaluate(val=val)
            or self.left.evaluate(val=val)
        )
