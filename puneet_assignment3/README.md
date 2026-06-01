# Puneet Assignment 3 (Python)

This folder contains two beginner-friendly Python scripts that demonstrate:

- **`factorial.py`**: factorial calculation using both **iteration** and **recursion**
- **`math_module_usage.py`**: usage of Python’s built-in **`math`** module (sqrt, log, sin)

Both scripts are designed to be run directly from the command line and prompt the user for input.

---

## Repository / Folder Structure

```text
learningpython/puneet_assignment3/
├── factorial.py
├── math_module_usage.py
└── README.md
```

---

## Prerequisites

- Python **3.x**
- No third-party dependencies (standard library only)

---

## How to Run

> Run commands from the repository root: `d:/learning_python/learningpython`

### 1) Run `factorial.py`

**What it does**
- Reads an integer from the user.
- Computes factorial (`n!`) using:
  - `factorial_iterative(n)`
  - `factorial_recursive(n)`
- Prints both results.

**Command**
```bash
python puneet_assignment3/factorial.py
```

**Example**
- Input: `5`
- Output includes:
  - `Factorial of 5 using iteration is: 120`
  - `Factorial of 5 using recursion is: 120`

**Notes for developers**
- Currently, inputs are not validated. If you want safer behavior, add checks such as:
  - factorial for non-negative integers only
- To reuse logic from another module, import the functions:
  - `from puneet_assignment3.factorial import factorial_iterative, factorial_recursive`

---

### 2) Run `math_module_usage.py`

**What it does**
- Reads a number from the user.
- Computes and prints:
  - `math.sqrt(num)`
  - `math.log(num)` (natural logarithm)
  - `math.sin(num)` (expects **radians**)

**Command**
```bash
python puneet_assignment3/math_module_usage.py
```

**Notes for developers**
- `math.log(num)` requires `num > 0` (otherwise Python raises a `ValueError`).
- `math.sin(num)` expects **radians**, not degrees.
  - If you have degrees, convert using: `math.radians(deg)`

---

## Code Overview (Developer Notes)

### `factorial.py`
- Uses two approaches:
  - **Iteration**: loops from 1 to `n` and multiplies into `result`
  - **Recursion**: base case `0/1 -> 1`, otherwise `n * factorial_recursive(n-1)`
- Execution starts immediately after reading user input.

### `math_module_usage.py`
- Demonstrates standard library calls from `math`.
- Execution starts immediately after reading user input.

---

## Recommended Improvements (Optional)

If you plan to extend this folder for more “production-like” development, consider:

1. Add a `main()` function and a guard:
   - `if __name__ == "__main__": main()`
2. Add input validation:
   - factorial: ensure non-negative integers
   - math: ensure log input is positive
3. Add unit tests (e.g., using `unittest` or `pytest`) for:
   - factorial results
   - math computations

---

## Quick Verification Checklist

- [ ] `python puneet_assignment3/factorial.py` runs and prints factorial using both methods
- [ ] `python puneet_assignment3/math_module_usage.py` runs and prints sqrt/log/sin for valid inputs

