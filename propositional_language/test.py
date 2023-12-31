from atom import Atom
from negation import Negation
from conjunction import Conjunction
from disjunction import Disjunction
from implication import Implication
from bidirectional import Bidirectional


from truth_table import TruthTable


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

# t = TruthTable(prop=final_proposition)
# print(t)
# print(t.satisfiability())


X = Conjunction()
print(X)
X.left = A
print(X)
X.right = B
print(X)