# Puneet Assignment 4

This folder contains two Python programs related to **file handling**:

- `appendfile.py` – writes user input to a file, appends extra text to the same file, then reads and prints the final contents.
- `readfileandhandleerror.py` – reads `sample.txt` and prints it line-by-line, while handling `FileNotFoundError` gracefully.

A sample input file is also included:

- `sample.txt` – text content that `readfileandhandleerror.py` reads.

And there is an output file created/updated by `appendfile.py`:

- `output.txt` – the file where `appendfile.py` writes and appends data.

---

## 1) `appendfile.py`

### What it does
1. Prompts the user for a line of text.
2. Creates/overwrites `output.txt` and writes the user input + newline.
3. Appends an additional line to the same `output.txt`.
4. Reads `output.txt` and prints the final content.

### How to run
```bash
python appendfile.py
```

### Notes for developers
- The script currently uses **absolute paths** pointing to `D:\learning_python\learningpython\puneet_assignment4\...`.
- If you move the project to another machine/folder, update the paths or refactor to use paths relative to the script directory (recommended).

---

## 2) `readfileandhandleerror.py`

### What it does
1. Opens `sample.txt`.
2. Prints the file content line-by-line (with line numbers).
3. If `sample.txt` is missing, it catches `FileNotFoundError` and prints a friendly message.

### How to run
```bash
python readfileandhandleerror.py
```

### Notes for developers
- Like the other script, it currently uses **absolute paths** for `sample.txt`.
- For future-proofing, refactor to use relative paths.

---

## Recommended refactor (for future development)
If you plan to enhance these programs, consider replacing absolute paths with a path derived from the current script location:

- Use `pathlib.Path(__file__).resolve().parent` to build the correct file path.
- This makes the code portable across different systems and directory layouts.

---

## Quick workflow
1. Run `readfileandhandleerror.py` to see `sample.txt`.
2. Run `appendfile.py`, enter some text, and then check `output.txt` for the appended content.

