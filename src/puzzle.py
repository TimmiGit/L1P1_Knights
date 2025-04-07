from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(
        AKnight, (And(AKnight, AKnave))
    ),  # If A is a knight, then A is not a night and a knave
    Implication(
        AKnave, Not(And(AKnight, AKnave))
    ),  # If A is a knave, then A is not a night and a knave
)
# print(model_check(knowledge0, AKnave))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(
        AKnight, And(AKnave, BKnave)
    ),  # A's statement is a lie if A is a knight
    Implication(
        AKnave, Not(And(AKnave, BKnave))
    ),  # If A is a knave, the statement is false, so at least one is not a knave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(
        AKnight, And(AKnight, BKnight)
    ),  # If A is a knight, A and B must be of the same kind
    Implication(
        AKnave, Not(And(AKnave, BKnave))
    ),  # If A is a knave, A and B must be of different kinds
    Implication(
        BKnight, Or(AKnight, BKnight)
    ),  # If B is a knight, A and B must be the same kind
    Implication(BKnight, Not(And(AKnight, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(
        AKnave, Not(Or(AKnight, AKnave))
    ),  # If A is a knave, then A can’t say "I am a knight or I am a knave" truthfully
    Implication(
        BKnight, And(AKnave, CKnave)
    ),  # B says "A is a knave and C is a knave" (true if B is a knight)
    Implication(
        BKnave, Not(And(AKnave, CKnave))
    ),  # B says "A is a knave and C is a knave" (false if B is a knave)
    Implication(CKnight, AKnight),  # C says "A is a knight" (true if C is a knight)
    Implication(CKnave, Not(AKnight)),  # If C is a knave, then A must be a knave
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]

    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
