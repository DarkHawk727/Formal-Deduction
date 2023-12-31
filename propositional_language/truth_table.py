from enum import Enum, auto
from itertools import product
from typing import List, Tuple

from tabulate import tabulate
from text_styles import TextStyle

from formula import Formula
from atom import Atom
from negation import Negation
from disjunction import Disjunction
from conjunction import Conjunction


class SemanticStatus(Enum):
    SATISFIABLE = auto()
    TAUTOLOGY = auto()
    CONTRADICTION = auto()


class TruthTable:
    def __init__(self, prop: Formula, domain: List[bool] = [True, False]) -> None:
        self._atoms: List[str] = list(prop.variables())
        self._header: List[str] = self._atoms + [
            TextStyle.BOLD + "RESULT" + TextStyle.ENDC
        ]
        self._table: List[List[bool]] = []
        self._prop_str: str = str(prop)

        for truth_val in product(domain, repeat=len(self._atoms)):
            tv: List[bool] = list(truth_val)
            result = prop.evaluate(dict(zip(list(self._atoms), tv)))
            self._table.append(tv + [result])

    def __repr__(self) -> str:
        printable: List[List[str]] = []
        for row in self._table:
            new_row: List[str] = []
            for elem in row:
                if elem:
                    new_row.append(TextStyle.GREEN + str(elem) + TextStyle.ENDC)
                else:
                    new_row.append(TextStyle.RED + str(elem) + TextStyle.ENDC)
            printable.append(new_row)

        print(f"Proposition: {self._prop_str}")
        print(
            tabulate(
                tabular_data=printable, headers=self._header, tablefmt="fancy_grid"
            )
        )
        return ""

    def __getitem__(self, i: int) -> Tuple[bool, ...]:
        return tuple(self._table[i])

    def satisfiability(self) -> SemanticStatus:
        results = [row[-1] for row in self._table]

        if all(results):
            return SemanticStatus.TAUTOLOGY
        elif any(results):
            return SemanticStatus.SATISFIABLE
        else:
            return SemanticStatus.CONTRADICTION  

    def disjunctive_normal_form(self) -> Formula:
        for row in self._table:
            if row[-1]:
                for index, variable in enumerate(self._atoms):
                    if row[index]:
                        temp: Atom = Atom(name=variable)
                        # Append the conjunction
                        pass
                    else:
                        temp: Formula = Negation(right=Atom(name=variable))
                        # Append the negation
                        pass
                pass
            # Append tha   temp with a disjunction
        return None
