
# Changelog

This file lists the main changes in Polynom Hunter.

## v0.2.0 — Incremental Degree Search

### Added

- Search degrees from 1 to `N - 1`, one by one.
- Store row operations in an `N × N` matrix `E`.
- Reuse those operations when adding a new power of `x`.
- Check the current degree using `E @ y` and `np.allclose`.
- Return coefficients from highest degree to lowest.
- Move the algorithm into `find_coefficients(x, y)`.
- Use NumPy for matrix operations.
- Add `requirements.txt` and three basic tests.

### Tested

- Tests for linear, quadratic, and cubic polynomials are included.
- No speed or memory comparison has been done yet.

### Known Limits

- Degree 0 is not tested separately.
- At least two points with different `x` values are assumed.
- Input validation is not included.
- Floating-point errors can change the result.
- The full `N × N` matrix `E` is still stored in memory.

### Next

- Test more types of input data.
- Study numerical errors.
- Compare v0.1.0 and v0.2.0 on the same data.

## v0.1.0 — First Version

### Added

- Read data points from CSV.
- Build the full Vandermonde matrix.
- Write Gauss–Jordan elimination (RREF) in Python.
- Find and print polynomial coefficients.
- Add the first README and project notes.

### Known Limits

- Always uses the full interpolation matrix.
- Uses `O(N³)` time and `O(N²)` memory for dense elimination.
- Floating-point calculations may cause errors.
