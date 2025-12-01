from solver import solve
from board import Board

if __name__ == '__main__':
    print('Pronlem N królowych - test ')
    testy = [1, 2, 3 ,4 ,5 ,6 ,7, 8]
    for n in testy:
        amount = solve(n)
        print(f'{n:2d} królowych {amount:3d} rozwiązań')
    
    print('\nPrzykładowe rozwiązanie dla 8 królowych: ')
    b = Board(8)
    solution = [0, 4, 7, 5, 2, 6, 1, 3]
    for col, row in enumerate(solution):
        b.place(row, col)
    print(b)
    