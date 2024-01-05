from atom import Atom
from conjunction import Conjunction
from disjunction import Disjunction
from formula import Formula
from negation import Negation
from truth_table import TruthTable

from typing import List, Tuple, Union

Literal = Union[Atom, Negation]
Clause = Union[Conjunction, Literal]
DNF = Union[Clause, Disjunction]


def build_clause(inp: List[Tuple[str, bool]]) -> Clause:
    def create_literal(name: str, val: bool) -> Literal:
        a: Atom = Atom(name=name)
        return a if val else Negation(right=a)

    if len(inp) == 1:
        return create_literal(*inp[0])
    else:
        first_atom: Literal = create_literal(*inp[0])
        if len(inp) == 2:
            second_atom: Literal = create_literal(*inp[1])
            return Conjunction(left=first_atom, right=second_atom)

    return Conjunction(left=first_atom, right=build_clause(inp[1:]))


def extract_clauses(t: TruthTable) -> List[Clause]:
    clauses: List[Clause] = []
    for row in t:
        if row["RESULT"]:
            clauses.append(
                build_clause(
                    inp=[(name, val) for name, val in row.items() if name != "RESULT"]
                )
            )
    return clauses


def disjunctive_normal_form(clauses: List[Clause]) -> DNF:
    if len(clauses) == 1:
        return clauses[0]
    else:
        first_arg = clauses[0]
        if len(clauses) == 2:
            second_arg = clauses[1]
            return Disjunction(left=first_arg, right=second_arg)

    return Disjunction(
        left=first_arg, right=disjunctive_normal_form(clauses=clauses[1:])
    )


def get_DNF(form: Formula) -> DNF:
    return disjunctive_normal_form(clauses=extract_clauses(t=TruthTable(prop=form)))
