"""

1 - Boş olan yeri seç
2 - (1-9) arasındaki rakamları bu boşluğa yerleştirmeye çalış
3 - Mevcut panoya göre o rakamın mevcut noktada geçerli olup olmadığını kontrol edin.
4 - a. Rakam geçerliyse, 1-3 adımlarını kullanarak panoyu tekrar tekrar doldurmaya çalışın.
    b. Geçerli değilse, az önce doldurduğunuz kareyi sıfırlayın ve bir önceki adıma dönün.

"""

import numpy as np

sudoku1 = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

sudoku = [
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 1, 0, 9, 2],
    [0, 0, 2, 0, 0, 0, 0, 8, 0],
    [2, 0, 0, 0, 5, 0, 0, 0, 3],
    [6, 0, 8, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 4, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 2, 6, 0, 0, 0],
    [0, 0, 4, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 5, 0]
]

sudoku = np.array(sudoku)
print("    Örnek Sudoku")
print(sudoku)
print("\n    Sudoku Çözüm")


def kontrol_et(y, x, n):
    global sudoku  # Recursion fonksiyon olduğu için global ile çağırılır

    for i in range(9):
        if sudoku[i][x] == n:
            return False

    for i in range(9):
        if sudoku[y][i] == n:
            return False

    rangeX = (x // 3) * 3  # |0 1 2 | 3 4 5 | 6 7 8 |
    rangeY = (y // 3) * 3  # 0       3       6

    
    for i in range(rangeX, rangeX + 3): # x = 0 => | 0  1 2  | ---- x = 3 => | 3 4 5| ---- x = 6 => | 6 7 8|
        for j in range(rangeY, rangeY + 3):
            if sudoku[j][i] == n:
                return False

    return True


def coz():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if kontrol_et(i, j, k):
                        sudoku[i][j] = k
                        coz()
                        sudoku[i][j] = 0
                return
    print(sudoku)


coz()
