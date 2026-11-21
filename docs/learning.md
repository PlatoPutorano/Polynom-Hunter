
## What I Learned

This is my first attempt at independently developing an algorithm for discovering polynomial relationships.

### Mathematics

- Formulating polynomial interpolation as a system of linear equations.
- Constructing the Vandermonde matrix and understanding its mathematical meaning.
- Proving the existence and uniqueness of an interpolating polynomial using the kernel of a linear transformation.
- Understanding the relationship between the number of polynomial roots, its degree, and the uniqueness of the solution.
- Applying RREF to calculate polynomial coefficients.

### Programming

- Implementing the Gauss-Jordan elimination algorithm in Python.
- Working with matrices represented as nested lists.
- Translating mathematical algorithms into working code.

### Key Takeaway

The most important thing I learned was how to turn a mathematical problem into a working algorithm.

I also realized that finding a polynomial that passes through all given points is not the same as finding the simplest polynomial that describes the underlying relationship.

This distinction will be one of the main directions for the future development of the project.

---

## What I Learned in v0.2.0

### Mathematics

- Adding a new column to the Vandermonde matrix when the degree grows.
- Building elementary matrices from row operations.
- Keeping earlier row operations in one matrix `E`.
- Understanding why the reduced matrix has an identity block.
- Using row operations to check whether a linear system has a solution.
- Understanding the difference between exact mathematics and floating-point calculations.

### Python and NumPy

- Creating arrays with `np.array` and identity matrices with `np.eye`.
- Using `@` to multiply a matrix and a vector.
- Working with rows using NumPy indexing and slicing.
- Swapping rows without changing their values by mistake.
- Understanding `.copy()` and NumPy views.
- Using `np.allclose` to check values with a tolerance.
- Returning polynomial coefficients in the correct order.

### Research

- Reusing calculations instead of starting from zero at every step.
- Testing code with polynomials whose coefficients are known.
- Checking whether the code follows the mathematical idea.
- Learning that a few successful tests do not prove that an algorithm always works.
- Understanding that I need measurements before saying one method is faster.

### What I Want to Learn Next

- How to choose better pivots and tolerances.
- How floating-point errors affect larger problems.
- Which version is faster and how much memory each one uses.
- Whether I can avoid storing the full matrix `E`.

### Main Lesson

In v0.1.0, I solved the full system. In v0.2.0, I learned how to add one column at a time and reuse earlier row operations. I still need to test the new method on more data.
