# Puneet Assignment 3 (Python)

This folder contains two small Python programs as part of **Assignment 3**:

1. **factorial.py** — Computes the factorial of a user-provided number using both **iteration** and **recursion**.
2. **math_module_usage.py** — Demonstrates the use of Python’s built-in **`math`** module (square root, natural log, and sine).

## Requirements

- Python 3.x
- No external libraries are required (uses only the standard library).

## Folder Structure

```
learningpython/puneet_assignment3/
├── factorial.py
├── math_module_usage.py
└── README.md
```

## How to Run

All programs are simple scripts (they prompt for input using `input()`), so you run them directly with Python.

### 1) factorial.py

**Purpose:**
- Read an integer `num` from the user.
- Compute `num!` using:
  - **Iteration** (`factorial_iterative`)
  - **Recursion** (`factorial_recursive`)

**Run command (from the project root `d:/learning_python/learningpython`):**

```bash
python puneet_assignment3/factorial.py
```

**Example input/output:***
- Input: `5`
- Output includes:
  - `Factorial of 5 using iteration is: 120`
  - `Factorial of 5 using recursion is: 120`

**Notes for modification:**
- To reuse the functions in another program, import them:
  - `from puneet_assignment3.factorial import factorial_iterative, factorial_recursive`
- If you want to handle negative numbers, add validation before computing.

### 2) math_module_usage.py

**Purpose:**
- Read a number from the user.
- Use the standard library `math` module to compute:
  - `math.sqrt(num)` (square root)
  - `math.log(num)` (natural logarithm)
  - `math.sin(num)` (sine of `num` in radians)

**Run command (from the project root `d:/learning_python/learningpython`):**

```bash
python puneet_assignment3/math_module_usage.py
```

**Notes for modification:**
- `math.log(num)` is only defined for `num > 0`.
- `math.sin(num)` expects **radians**, not degrees. Convert degrees using `math.radians(deg)` if needed.

## Code Style & Understanding

- Both scripts are intentionally straightforward for learning purposes.
- Functions include docstrings that explain what they do.
- Both scripts are written as runnable entrypoints; they execute immediately after prompting for input.

## Tips for Further Improvements (Optional)

If you want to make the programs more robust and reusable:

- Add a `__name__ == "__main__"` guard so the code only runs when executed directly.
- Validate user input (e.g., ensure factorial input is a non-negative integer; ensure log input is positive).
- Convert scripts into a module-style design (move input/output handling into `main()`).

