# Formal Deduction

This is a Python program to allow me to perform some operations with propositional and first-order logic. It let's me define arbitrary propositions either programatically or through a plaintext representation. It can then create a truth table and determine its satisfiability.

## Current Features

- Define arbitrary statements in propositional language either programatically.
- Lets you evaluate statements with a valuation
- Create a truth table for said proposition, determine satisfiability, check if two propositions are logically equivalent.
- Generate the Disjunctive Normal Form of a proposition by truth table.

## Planned Features

- Parse expressions from a plaintext representation using a recursive descent parser.
- Show intermediate results in truth tables.
- Define rules to transform expressions like (A → B) ≡ ((¬A) ∨ B)
- Resolution using DPP

## Useful Links

- Recursive Descent Parser for Parsing propositions https://stackoverflow.com/questions/9785553/how-does-a-simple-calculator-with-parentheses-work
- LogicThruPython
- https://github.com/joedougherty/sentential
- https://www.engr.mun.ca/~theo/Misc/exp_parsing.htm
