from __future__ import annotations
from enum import Enum, auto
from itertools import product
from typing import Dict, Iterator, List, Tuple

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
        self._header: List[str] = self._atoms + ["RESULT"]
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
        printable_headers: List[str] = self._header
        printable_headers[-1] = TextStyle.BOLD + "RESULT" + TextStyle.ENDC
        print(
            tabulate(
                tabular_data=printable, headers=printable_headers, tablefmt="fancy_grid"
            )
        )
        return ""

    def __getitem__(self, i: int) -> List[bool]:
        return self._table[i]

    def __iter__(self) -> Iterator[Dict[str, bool]]:
        for row in self._table:
            yield dict(zip(self._header, row))

    # This seems too naive an approach since the headers can be in a different order.
    def __eq__(self, other: object) -> bool:
        if isinstance(other, TruthTable):
            if len(self._table) != len(other._table):
                return False
            else:
                for i in range(len(self._table)):
                    if self._table[i] != other._table[i]:
                        return False
                return True
        raise NotImplementedError

    def satisfiability(self) -> SemanticStatus:
        results = [row[-1] for row in self._table]

        if all(results):
            return SemanticStatus.TAUTOLOGY
        elif any(results):
            return SemanticStatus.SATISFIABLE
        else:
            return SemanticStatus.CONTRADICTION
