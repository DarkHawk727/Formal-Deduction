from connectives import Connective
from formula import Formula


class Conjunction(Formula):
    con = Connective.AND

    def __init__(self, lhs: Formula, rhs: Formula) -> None:
        self.left = lhs
        self.right = rhs

    def __str__(self) -> None:
        return f"Conjunction(left={str(self.left)}, right={str(self.right)})"

    def truth_val(self) -> bool:
        return (self.left).truth_val() & (self.right).truth_val()
