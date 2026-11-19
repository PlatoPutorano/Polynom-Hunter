import csv

def to_rref(matrix: list[list[float]]) -> list[list]:
    M = [[float(num) for num in row] for row in matrix]

    rows = len(M)
    cols = len(M[0])
    lead = 0

    for r in range(rows):
        if lead >= cols:
            break

        i = r
        while abs(M[i][lead]) < 1e-10:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return M

        M[i], M[r] = M[r], M[i]

        pivot = M[r][lead]
        M[r] = [m / pivot for m in M[r]]

        for i in range(rows):
            if i != r:
                factor = M[i][lead]
                M[i] = [M[i][j] - factor * M[r][j] for j in range(cols)]

        lead += 1

    for r in range(rows):
        for c in range(cols):
            if abs(M[r][c]) <1e-10:
                M[r][c] = 0.0

    return M

def read_csv(path: str) -> tuple[list[float], list[float]]:
    x = []
    y = []

    with open(path, 'r', newline="", encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            x.append(float(row['x']))
            y.append(float(row['y']))
    return x, y

x, y = read_csv('data.csv')

n = len(x)

A = []

for row in range(0, n):
    A.append([])
    for deg in range(0, n):
        A[row].append(x[row] ** deg)

matrix = A

for i in range(0, n):
    matrix[i].append(y[i])

result = to_rref(matrix)

a = []

for i in range(0, n):
    for j in range(n, n + 1):
        a.append(result[i][j])
a.reverse()
print(a)