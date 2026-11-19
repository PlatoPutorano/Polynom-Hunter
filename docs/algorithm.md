# Polynomial Interpolation — v0.1.0

## 1. Problem

Given n points (x_i, y_i) with pairwise distinct
x-coordinates, find a polynomial P such that:

P(x_i) = y_i for every i.

## 2. Polynomial Representation

We consider:

P(x) = a_0 + a_1*x + ... + a_(n-1)*x^(n-1)

The unknowns are the coefficients a_0, ..., a_(n-1).

## 3. Linear System

Substituting the observed x-coordinates into P
produces a linear system:

A * a = y

where A is the Vandermonde matrix:

A[i][j] = x_i^j

using zero-based indexing.

## 4. Existence and Uniqueness

The matrix A is invertible when all x_i are distinct.

Proof:

Assume A*a = 0.

The corresponding polynomial P has n distinct roots,
while its degree is at most n-1.

Therefore P must be the zero polynomial.

Hence all coefficients are zero:

ker(A) = {0}

Since A is an n-by-n matrix, it is invertible.

Thus the system A*a = y has a unique solution.

## 5. Computational Method

We construct the augmented matrix:

[A | y]

Then we apply Gauss-Jordan elimination.

In exact arithmetic, the resulting RREF is:

[I | a]

The final column contains the polynomial coefficients.

## 6. Numerical Limitations

The implementation uses floating-point arithmetic
and a fixed tolerance of 1e-10.

This can cause inaccurate results, particularly for
ill-conditioned Vandermonde matrices.

Numerical stability will be investigated in later
versions.