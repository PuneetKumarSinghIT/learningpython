# Assignment 1 — Basic Python Programs

This folder contains two simple Python programs that demonstrate basic user input and printing output.

## Files
- **`arithmetic_task.py`** — Takes two numbers as input and prints addition, subtraction, multiplication, and division.
- **`greeting.py`** — Takes a first name and last name as input and prints a greeting.

## Requirements
- Python 3.x

## How to Run
Run the scripts from the project directory:

### 1) Arithmetic Task
**Command:**
```bash
python assignment_1/arithmetic_task.py
```
**What it does:**
- Prompts:
  - `Enter the first number: `
  - `Enter the second number: `
- Assumes both inputs are integers.
- Prints:
  - `Addition: <result>`
  - `Subtraction: <result>`
  - `Multiplication: <result>`
  - `Division: <result>` (rounded to 2 decimals)

**Division by zero note:**
- If the second number is `0`, it prints:
  - `Undefined (division by zero)`

### 2) Greeting Program
**Command:**
```bash
python assignment_1/greeting.py
```
**What it does:**
- Prompts:
  - `Enter your first name: `
  - `Enter your last name: `
- Prints a message like:
  - `Hello, <First Last>! Welcome to learning Python!`

## Tips for Working With the Code
- Each script uses `input()` to collect values from the user.
- `arithmetic_task.py` converts inputs using `int(...)`, so entering non-numeric text will raise an error.
- Output is printed directly using `print()`.

