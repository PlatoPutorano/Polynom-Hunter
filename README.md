
# Polynom Hunter

Polynom Hunter is a small research project about finding polynomial formulas from data points.

## Long-Term Goal

I want to build an algorithm that finds a simple polynomial for a given set of points.

The first version solves a full interpolation problem. For `N` points, it finds a polynomial of degree at most `N - 1`. But the points may come from a much simpler polynomial.

For example, if 1,000 points come from `P(x) = 2x + 1`, I want to find that simple formula without solving a full `1000 × 1000` system.

My goals are to:

- Find a polynomial with a low degree.
- Reuse calculations when the degree grows.
- Study the time, memory use, and accuracy of different methods.
- Later, work with noisy data.

## Current Version: v0.2.0

Version 0.2.0 adds **incremental degree search**.

The code starts with a column of ones. It then adds columns for `x`, `x²`, `x³`, and so on. It stores row operations in a matrix `E` and reuses them for the next column.

### Implemented

- Read points from `data.csv`.
- Try polynomial degrees from `1` to `N - 1`.
- Build each new column from the values of `x`.
- Store and update row operations in `E`.
- Check whether the current degree fits the points.
- Return coefficients in order from highest degree to lowest.
- Use NumPy for array and matrix operations.

The main algorithm is in `find_coefficients(x, y)` in `main.py`.

**Note:** the code does not check degree 0. For constant data with at least two different `x` values, it can return an array for degree 1 with a zero coefficient for `x`.

### Previous Version: v0.1.0

The first version:

- Read points from CSV.
- Built the full Vandermonde matrix.
- Used my own Gauss–Jordan elimination (RREF).
- Found and printed polynomial coefficients.

See [Algorithm Documentation](docs/algorithm.md) and [Changelog](CHANGELOG.md).

## Mathematical Approach

We have `N` points `(x_i, y_i)` with different `x` values. We look for a polynomial

$$
P(x) = a_0 + a_1x + \cdots + a_mx^m
$$

such that `P(x_i) = y_i` for all points. This gives a linear system:

$$
A_m a = y.
$$

In v0.2.0, I keep a matrix `E` that stores the row operations. In exact arithmetic, after processing degree `m`,

$$
E A_m = \begin{pmatrix} I_{m+1} \\ 0 \end{pmatrix}.
$$

I then calculate `b = E @ y`. If all entries in `b[m+1:]` are zero, a polynomial of degree at most `m` fits the points.

The code checks this with `np.allclose`, so the result depends on a numerical tolerance. See [docs/algorithm.md](docs/algorithm.md) for details.

## Installation

You need:

- Python 3.9 or newer.
- NumPy.

Install NumPy from `requirements.txt`:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Put your points in `data.csv` with columns `x` and `y`, for example:

```csv
x,y
1,3
2,5
3,7
```

Run the program from the project folder:

```bash
python3 main.py
```

Expected output:

```text
[2. 1.]
```

This means `P(x) = 2x + 1`. Coefficients are printed from the highest degree to the lowest.

Run the three basic tests with:

```bash
python3 -m unittest discover -s tests -v
```

## Limitations

### 1. Time and Memory

- v0.1.0 uses `O(N³)` time and `O(N²)` memory for dense Gauss–Jordan elimination.
- v0.2.0 stores an `N × N` matrix `E`, so it still uses `O(N²)` memory.
- If v0.2.0 stops at degree `d`, its work is about `O(N²d)`. In the worst case, this is `O(N³)`.
- I have not compared the running times yet.

### 2. Numerical Accuracy

- The mathematical method assumes exact calculations, but NumPy uses floating-point numbers.
- The code uses the first pivot for which `w[i] != 0`. A very small pivot can cause errors.
- The degree check uses `np.allclose` with `atol=1e-10` and `rtol=0`.
- The code can return the wrong degree or coefficients because of rounding errors.

### 3. Polynomial Degree and Input

- The code checks degrees `1` through `N - 1`, not degree 0.
- It assumes at least two points and different `x` values.
- It does not check input errors or handle noisy data.
- If the numerical degree check never succeeds, `find_coefficients` returns `None`.

## Roadmap

### 1. What We Have Accomplished

I have written two versions of polynomial interpolation:

- **v0.1.0:** solve one full Vandermonde system.
- **v0.2.0:** add one column at a time and reuse row operations.

Three basic tests for degrees 1, 2, and 3 are included. They are not enough to prove that the code works for every input.

### 2. What We Want to Improve

Next, I want to:

- Test the code on more polynomial examples.
- Study numerical errors and pivot selection.
- Compare time and memory use between v0.1.0 and v0.2.0.
- Find out whether I can store less data than the full matrix `E`.

### 3. Handling Noisy Data

For now, I work with points that should fit a polynomial exactly. Later, I want to learn polynomial approximation and work with noisy data.

### 4. Benchmarking and Research

I plan to measure speed, memory use, and errors. I will use the same data for both versions to make the comparison fair.

## Project Status

**v0.2.0 is an experimental version.** The basic tests cover only a few examples. The speed comparison is planned for later.

## Learning Log

[What I Learned — v0.1.0 and v0.2.0](docs/learning.md)

## Version History

[Changelog](CHANGELOG.md)
