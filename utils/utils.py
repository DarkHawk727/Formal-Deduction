from propositional_language.truth_table import TruthTable
from propositional_language.formula import Formula


def semantically_equivalent(prop_1: Formula, prop_2: Formula) -> bool:
    return TruthTable(prop=prop_1) == TruthTable(prop=prop_2)
