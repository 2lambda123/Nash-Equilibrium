from nash_grid import NashGrid

pd = NashGrid("../tests/pd.txt")
print("test file 1:")
print(pd.payout_grid)
print(pd.col_labels)
print(pd.remove_dominated_moves())
print(pd.payout_grid)

pd2 = NashGrid("../tests/pd2.txt")
print("test file 2:")
print(pd2.payout_grid)
print(pd2.col_labels)
print(pd2.remove_dominated_moves())
print(pd2.payout_grid)

pd3 = NashGrid("../tests/pd3.txt")
print("test file 3:")
print(pd3.payout_grid)
print(pd3.col_labels)
print(pd3.remove_dominated_moves())
print(pd3.payout_grid)