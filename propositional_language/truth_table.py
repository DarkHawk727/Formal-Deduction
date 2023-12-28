from enum import Enum, auto
from itertools import product
from typing import Any, List

from atom import Atom
from bidirectional import Bidirectional
from conjunction import Conjunction
from disjunction import Disjunction
from formula import Formula
from implication import Implication
from negation import Negation


# Assuming the Atom, Negation, Conjunction, Disjunction, Implication, and Bidirectional classes are already defined
A = Atom("A")
B = Atom("B")
C = Atom("C")
D = Atom("D")

final_proposition = Bidirectional(
    left=D,
    right=Implication(
        left=D,
        right=Disjunction(left=C, right=Conjunction(left=B, right=Negation(right=A))),
    ),
)


class TruthTable:
    class Satisfiability(Enum):
        SATISFIABLE = auto()
        TAUTOLOGY = auto()
        CONTRADICTION = auto()

    def __init__(self, prop: Formula, domain: List[bool] = [True, False]) -> None:
        atoms: List[str] = list(prop.variables()) + ["RESULT"]
        self.table: List[List[bool | str]] = [atoms]

        for truth_val in product(domain, repeat=len(atoms)):
            tv: List[bool] = list(truth_val)
            self.table.append(tv + [str(prop.evaluate(dict(zip(atoms, tv))))])

    def __str__(self) -> str:
        result = ""
        for row in self.table:
            for elem in row:
                result += str(elem) + " "
            result += "\n"
        return result

    def satisfiability(self) -> str:
        raise NotImplementedError


t = TruthTable(prop=final_proposition)
print(t)
