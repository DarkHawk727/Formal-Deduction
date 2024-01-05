

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


print(get_DNF(form=final_proposition))
"""
A -> B -> C
not A v (B -> C)

Traverse the rule tree and the expressin tree, matching the lefts, and rights.
If we see an atom, add it to the HashMap
"""
