from __future__ import annotations

from connectives import Connective

CONNECTIVES_MAP = {
    Connective.NEG: lambda a: not a,
    Connective.AND: lambda l,r: l & r,
    Connective.OR: lambda l,r: l | r,
    Connective.TO: lambda l,r: (not l) | r,
    Connective.IFF: lambda l,r: l & r,
}

class Formula():
    def __init__(self, lhs: Formula, rhs: Formula, con: Connective) -> None:
        self.left = lhs
        self.right = rhs
        self.con = con

    def __str__(self) -> None:
        return f"{self.con.name}(left={str(self.left)}, right={str(self.right)})"
    
    def __not__(self) -> bool:
        raise NotImplementedError
    
    def __and__(self, other: Formula) -> bool:
        pass
    
    def truth_val(self) -> bool:
        CONNECTIVES_MAP[self.con]((self.left).truth_val(), (self.right).truth_val())


