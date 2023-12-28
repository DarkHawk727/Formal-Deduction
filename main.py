from formula.connectives import *

A = Atom(name="A", value=False)
B = Atom(name="B")
C = Atom(name="C", value=False)
D = Atom(name="D")

E = Conjunction(left=A, right=B)
F = Implication(left=E, right=C)


def list_atoms(formula: Formula) -> Set[str]:
    atoms: Set[str] = set()

    if isinstance(formula, Atom):
        atoms.add(formula.name)
    elif isinstance(formula, Negation):
        atoms.update(list_atoms(formula.right))
    elif isinstance(formula, (Conjunction, Disjunction, Implication, Bidirectional)):
        atoms.update(list_atoms(formula.left))
        atoms.update(list_atoms(formula.right))

    return atoms


# Example usage with your provided formulas
atoms_in_F = list_atoms(F)
print("Atoms in proposition F:", atoms_in_F)
