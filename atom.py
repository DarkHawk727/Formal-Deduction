from __future__ import annotations


class Atom:
    def __init__(self, name: str, value: bool = True) -> None:
        self.name = name
        self.value = value

    def __eq__(self, other: Atom) -> bool:
        return self.name == other.name and self.value == other.value
    
    def __neg__(self) -> Atom:
        return Atom(self.name, not self.value)

    def __str__(self) -> str:
        return f"Atom(name={self.name}, value={self.value})"



a = Atom("A")
print(a)
print(a.name)
print(a.value)
print(-a)