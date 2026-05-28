# Puneet Assignment 2

This folder contains two small Python programs:

- `even_odd.py` – checks whether a user-provided integer is even or odd.
- `sum_of_integers.py` – calculates the sum of integers from 1 to 50.

All scripts are standalone (no external dependencies) and run using Python 3.

---

## Prerequisites

- Python 3.x installed

To verify:

```bash
python --version
```

---

## 1) `even_odd.py` (Even / Odd Checker)

### What it does

- Takes an integer input from the user
- Uses an `if-else` condition to determine whether the number is even or odd
- Prints the result

### How to run

From this folder:

```bash
python even_odd.py
```

### Example

Input:

```text
Enter an integer: 7
```

Output:

```text
7 is an odd number.
```

---

## 2) `sum_of_integers.py` (Sum from 1 to 50)

### What it does

- Iterates over numbers from 1 to 50 using a loop (`range(1, 51)`)
- Accumulates the total in `total_sum`
- Prints the final sum

### How to run

From this folder:

```bash
python sum_of_integers.py
```

### Example output

```text
The sum of integers from 1 to 50 is: 1275
```

---

## Notes for new developers

- These scripts are intentionally simple and meant for beginner practice.
- There are no shared modules or classes between the two programs.

