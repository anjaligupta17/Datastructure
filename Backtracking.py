def permute(list,s):
    if list==1:
        return s
    else:
        return
        [
            y+x
            for y in permute(1,s)
            for x in permute(list-1,s)
        ]

print(permute(1,["a","s","f"]))
print(permute(2,["a","s","f"]))
#example of it is:-Examples where backtracking can be used to solve puzzles or problems include: Puzzles such as eight queens puzzle, crosswords, verbal arithmetic, Sudoku, and Peg