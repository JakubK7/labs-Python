from __future__ import annotations
from typing import List, Tuple, Optional

class Board:
    # Szachownica do problemu N królowych.
    #  rekurencja po kolumnach.
    # queens[col] = row  → w danej kolumnie stoi królowa w tym wierszu
    
    def __init__(self, n: int = 8) -> None:
        self.n = n
        self.queens: List[Optional[int]] = [None] * n

    def place(self, row: int, col: int) -> None:
        # Umiaszcza któlowa z kolumny col 
        self.queens[col] = row

    def remove(self, row: int, col: int) -> None:
        self.queens[col] = None

    def is_safe(self, row: int, col: int) -> None:
        # Sprawdza czy mozna postawic królową w row col
        for prev_col in range(col):
            prev_row = self.queens[prev_col]
            if prev_row is None:
                continue
            if prev_row == row:
                return False
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True
    
    def solve(self) -> int:
        # Zwraca liczbe rozwiązań
        self.queens = [None] * self.n 

        def backtrack(col: int = 0) -> int:
            if col == self.n:
                return 1
            count = 0
            for row in range(self.n):
                if self.is_safe(row, col):
                    self.place(row, col)
                    count += backtrack(col + 1)
                    self.remove(row, col)
            return count
        return backtrack()
    
    def __str__(self) -> str:
        if all(q is None for q in self.queens):
            return "Empty board"
        lines = []
        for row in range(self.n -1, -1, -1):
            line = [f"{row + 1} "]
            for col in range(self.n):
                if self.queens[col] == row:
                    line.append(" Q ")
                else:
                    line.append(" . ")
            lines.append("".join(line))

        letters = " " + " ".join(chr(ord('a') + i) for i in range(self.n))
        lines.append(letters)

        return "\n".join(lines)

    
    def __repr__(self) -> str:
        placed = [(chr(ord('a')+ c), r + 1) for c, r in enumerate(self.queens) if r is not None]
        return f'Borard(n={self.n}, queens{placed})'
    
    def __len__(self) -> int:
        return self.n
    
    def __iter__(self):
        # Iteruje po parach kolumna, wiersz
        return ((col, row) for col, row in enumerate(self.queens)  if row is not None)
    
    def __contains__(self, pos: Tuple[int, int]) -> bool:
        col, row = pos
        return 0 <= col < self.n and self.queens[col] == row
        
        