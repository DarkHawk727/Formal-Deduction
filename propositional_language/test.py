from atom import Atom
from negation import Negation
from conjunction import Conjunction
from disjunction import Disjunction
from implication import Implication
from bidirectional import Bidirectional

from typing import Set
from formula import Formula

# Assuming the Atom, Negation, Conjunction, Disjunction, Implication, and Bidirectional classes are already defined
A = Atom("A")
B = Atom("B")
C = Atom("C")
D = Atom("D")

final_proposition = Bidirectional(
    left=D,
    right=Implication(
        left=D,
        right=Disjunction(left=C, right=Conjunction(left=B, right=Negation(right=A)))
    )
)

# Creating additional propositions
prop1 = Implication(
    left=Conjunction(left=A, right=B),
    right=Disjunction(left=C, right=D)
)

prop2 = Bidirectional(
    left=Negation(right=B),
    right=Conjunction(left=A, right=D)
)

prop3 = Conjunction(
    left=Implication(left=C, right=D),
    right=Disjunction(left=A, right=B)
)

# Creating a set and adding the propositions
x: Set[Formula] = set()
x.add(final_proposition)
x.add(prop1)
x.add(prop2)
x.add(prop3)

print(x)
# Now x is a set containing the four propositions


