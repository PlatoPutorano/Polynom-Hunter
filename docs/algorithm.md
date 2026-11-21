
# Polynomial Interpolation — Algorithms

## 1. The Problem

We have `N` points:

$$
(x_1,y_1),\ldots,(x_N,y_N).
$$

All `x_i` values are different. I want to find a polynomial that passes through every point.

For `N` different `x` values, there is exactly one polynomial of degree at most `N - 1` that fits the data.

The mathematical results below assume exact arithmetic. The Python code uses floating-point numbers.

## 2. The Vandermonde Matrix

For a degree at most `m`, write:

$$
P_m(x)=a_0+a_1x+\cdots+a_mx^m.
$$

The coefficients must satisfy:

$$
A_m a=y,
\qquad
A_m=\begin{pmatrix}
1&x_1&\cdots&x_1^m\\
1&x_2&\cdots&x_2^m\\
\vdots&\vdots&&\vdots\\
1&x_N&\cdots&x_N^m
\end{pmatrix}.
$$

`A_m` has `N` rows and `m + 1` columns.

If `m < N` and all `x_i` are different, the columns are linearly independent. Here is why:

If the columns were dependent, there would be a nonzero polynomial of degree at most `m` with all `N` values `x_i` as roots. But a nonzero polynomial of degree at most `m` cannot have more than `m` different roots. Since `m < N`, this is impossible.

So:

$$
\operatorname{rank}(A_m)=m+1.
$$

## 3. Version 0.1.0 — Full Interpolation

The first version builds the full `N × N` Vandermonde matrix and adds the `y` column:

$$
[A_{N-1}\mid y].
$$

It uses my own Gauss–Jordan elimination to reach RREF:

$$
[A_{N-1}\mid y]\longrightarrow[I_N\mid a].
$$

The last column gives the coefficients. The code prints them from the highest degree to the lowest.

A standard dense implementation uses `O(N³)` time and `O(N²)` memory. This version always works with the full system and does not search for a smaller degree.

## 4. Version 0.2.0 — Adding One Column at a Time

### 4.1. Main Idea

When the degree grows from `m - 1` to `m`, we add one column:

$$
A_m=[A_{m-1}\mid v_m],
\qquad
v_m=\begin{pmatrix}x_1^m\\\vdots\\x_N^m\end{pmatrix}.
$$

Instead of reducing the whole matrix again, the code keeps an `N × N` matrix `E` with the row operations already used.

After processing degree `m`, the goal is:

$$
\boxed{E_mA_m=\begin{pmatrix}I_{m+1}\\0\end{pmatrix}.}
$$

`E_m` is a product of elementary matrices. Each elementary matrix is invertible, so `E_m` is also invertible in exact arithmetic.

### 4.2. Start With Degree 0

The first column has only ones:

$$
A_0=\begin{pmatrix}1\\1\\\vdots\\1\end{pmatrix}.
$$

The code starts with `E = np.eye(N)` and subtracts the first row from every row below it. Then:

$$
E_0A_0=\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix}.
$$

This prepares the algorithm. **The current code does not check whether degree 0 already fits the data.**

### 4.3. Add a New Power

Suppose we have already processed degree `m - 1`:

$$
E_{m-1}A_{m-1}=\begin{pmatrix}I_m\\0\end{pmatrix}.
$$

The code creates `v = x ** m` and calculates:

$$
w=E_{m-1}v_m.
$$

It then:

1. Finds the first nonzero value in `w[m:]`.
2. Swaps that value with `w[m]` and swaps the same two rows of `E`.
3. Divides row `m` of `E` by the pivot value.
4. Uses row `m` to remove all other values from the new column.

The code uses zero-based Python indices: the first row has index `0`.

The old columns stay in the same reduced form. The new column becomes the next column of the identity block.

Why does a nonzero pivot exist? If every value in `w[m:]` were zero, then the new column would be in the span of the old columns. This would contradict the independence of the Vandermonde columns proved above.

This argument works in exact arithmetic when the `x` values are different.

### 4.4. Check the Degree

We need to solve:

$$
A_ma=y.
$$

Multiply by `E_m`:

$$
\begin{pmatrix}I_{m+1}\\0\end{pmatrix}a=E_my.
$$

Let `b = E @ y`. In exact arithmetic, a polynomial of degree at most `m` exists **if and only if** every entry in `b[m+1:]` is zero.

When this is true, the coefficients in increasing degree order are:

$$
a=(b_1,\ldots,b_{m+1})^T.
$$

The code checks the remaining entries with:

```python
np.allclose(b[m + 1:], 0, atol=1e-10, rtol=0)
```

If the check passes, it returns `b[:m + 1][::-1]`. The `[::-1]` part puts the highest-degree coefficient first.

The code checks degrees `1, 2, ..., N - 1` and stops at the first one that passes the numerical test. It does not test degree 0 separately.

### 4.5. Time and Memory

The `E` matrix needs `O(N²)` memory.

For each new degree, multiplying `E @ v` and changing the rows of `E` takes `O(N²)` operations. If the algorithm stops at degree `d`, the total is about `O(N²d)`. In the worst case, it is `O(N³)`.

We cannot say that v0.2.0 is faster until we measure both versions.

## 5. Code and Limitations

The algorithm is in `find_coefficients(x, y)` in `main.py`.

It uses NumPy for:

- `np.eye(N)` — creating the starting identity matrix.
- `E @ v` and `E @ y` — matrix-vector multiplication.
- Array indexing and slicing — row operations and row swaps.
- `np.allclose` — checking whether the remaining values are close to zero.

Important limits:

- The code assumes at least two points and different `x` values.
- It does not check invalid input.
- It chooses the first pivot that is not exactly zero, even if that value is very small.
- The `1e-10` tolerance may give a wrong result for some data.
- It does not handle noisy data.
- If no degree passes the numerical check, the function returns `None`.

## 6. Tests and Next Steps

The project includes three basic tests with known polynomials of degrees 1, 2, and 3. These tests only cover a few cases.

The next steps are to test more values of `x`, check numerical errors, and compare time and memory use with v0.1.0. The speed comparison has not been done yet.
