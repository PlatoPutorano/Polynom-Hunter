import csv
import numpy as np


def read_csv(path: str) -> tuple[list[float], list[float]]:
    x = []
    y = []

    with open(path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x.append(float(row['x']))
            y.append(float(row['y']))

    return x, y


def find_coefficients(x: np.ndarray, y: np.ndarray) -> np.ndarray:

    n = len(x)

    E = np.eye(n)
    for i in range(1, n):
        E[i, :] -= E[0, :]

    for m in range(n):
        if m > 0:
            v = x ** m
            w = E @ v

            pivot_row = None
            for i in range(m, n):
                if w[i] != 0:
                    pivot_row = i
                    break
            if pivot_row is None:
                raise ArithmeticError('No nonzero pivot found; check numerical stability')

            if pivot_row != m:
                w[m], w[pivot_row] = w[pivot_row], w[m]
                E[[m, pivot_row], :] = E[[pivot_row, m], :]

            E[m, :] /= w[m]
            for i in range(n):
                if i != m:
                    E[i, :] -= E[m, :] * w[i]

        b = E @ y
        if np.allclose(b[m + 1:], 0, atol=1e-10, rtol=0):
            return b[:m + 1][::-1]

    raise ArithmeticError('No polynomial found; check numerical stability')


if __name__ == '__main__':
    x_values, y_values = read_csv('data.csv')
    x = np.array(x_values)
    y = np.array(y_values)
    print(find_coefficients(x, y))