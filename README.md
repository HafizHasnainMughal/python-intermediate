# python-intermediate-

# 🐍 Master Python Fundamentals

A structured, beginner-to-advanced repository containing comprehensive Python examples, interactive scripts, and clean code demonstrations. This repository covers fundamental core concepts—from built-in data structures and functional programming tools to mathematical operations, randomness, file handling, modular code design, and robust exception handling.

---

## 📌 Topics Covered

This repository contains dedicated code examples covering the following key Python modules and concepts:

1. **Lists & List Operations** (`_10list.py`)
2. **Tuples** (`_11tuple.py`)
3. **Sets & Set Operations** (`_12set.py`)
4. **Dictionaries** (`_13dict.py`)
5. **Functions & Scope** (`_14function.py`)
6. **Lambda Functions** (`_15lambda.py`)
7. **Walrus Operator `:=`** (`_16walrus.py`)
8. **Sorting Algorithms & Keys** (`_17sorted.py`)
9. **Map Function** (`_18map.py`)
10. **Filter Function** (`_19filter.py`)
11. **Reduce Function** (`_20reduce.py`)
12. **Zip Function** (`_21zip.py`)
13. **Enumerate Function** (`_22enumerate.py`)
14. **Random Module & Mini-Game** (`_23random.py`)
15. **Math Module** (`_24math.py`)
16. **Exception Handling** (`_25exception.py`)
17. **File Handling & I/O** (`_26file_handling.py`)
18. **Modules & Code Reusability** (`_27modules.py`, `calculator.py`, `student.py`)
19. **Decorators & First-Class Functions** (`_28decorator.py`)
20. **List Comprehension** (`_29list_comprehension.py`)
21. **Dictionary Comprehension** (`_30dict_comprehension.py`)

---

## 🛠 Detailed Overview

### 1. Lists (`_10list.py`)

- **Key Concepts:** Ordered, mutable collections of mixed data types.
- **Features Covered:** Indexing, slicing, list mutation, and iteration using `for` and `while` loops.
- **Methods Demonstrated:** `append()`, `remove()`, `pop()`, `sort()`, `copy()`, `extend()`, `insert()`, and `clear()`.

### 2. Tuples (`_11tuple.py`)

- **Key Concepts:** Immutable, memory-efficient sequences ideal for fixed data structures.
- **Features Covered:** Single-element tuples, negative indexing, slicing, tuple packing/unpacking, and type conversion (`tuple` ↔ `list`).
- **Built-in Functions:** `len()`, `min()`, `max()`, and `sum()`.

### 3. Sets (`_12set.py`)

- **Key Concepts:** Unordered collections of unique elements.
- **Set Operations:** Union (`|`), Intersection (`&`), and Difference (`-`).
- **Advanced Features:** Copying sets, adding/removing items, and using `frozenset` for immutable sets.

### 4. Dictionaries (`_13dict.py`)

- **Key Concepts:** Key-Value store with unique, immutable keys and mutable values.
- **Features Covered:** Safe access with `.get()`, updating key-value pairs, iterating through `.keys()`, `.values()`, and `.items()`.
- **Nested Structures:** Lists inside dictionaries, dictionaries inside lists, and multi-level nested dictionaries.

### 5. Functions & Scope (`_14function.py`)

- **Key Concepts:** Reusable blocks of code designed for modular programming.
- **Function Types:** Built-in vs. User-defined functions.
- **Arguments Handling:** Standard parameters, default parameters, arbitrary positional arguments (`*args`), and keyword arguments (`**kwargs`).
- **Advanced Concepts:** Local vs. Global variable scope, recursion (Factorial & Fibonacci series).

### 6. Lambda Functions (`_15lambda.py`)

- **Key Concepts:** Anonymous, single-expression inline functions.
- **Features Covered:** Arithmetic operations, inline conditional statements (`if-else`), and nested lambda functions.

### 7. Walrus Operator (`_16walrus.py`)

- **Key Concepts:** Assignment expressions (`:=`) introduced in Python 3.8 to assign values to variables within larger expressions.
- **Use Cases:** Streamlining interactive user input loops without code duplication.

### 8. Custom Sorting (`_17sorted.py`)

- **Key Concepts:** In-place sorting using `.sort()` and creating new sorted iterables.
- **Advanced Techniques:** Sorting structured tuples and lists using custom key functions and `lambda` key extractors.

### 9. Functional Mapping (`_18map.py`)

- **Key Concepts:** Applying a transformation function to every element in an iterable using `map(function, iterable)`.
- **Use Cases:** Updating records (e.g., price percentage hikes) and applying mathematical transformations over entire datasets.

### 10. Data Filtering (`_19filter.py`)

- **Key Concepts:** Extracting elements from iterables based on conditional boolean checks.
- **Use Cases:** Filtering lists by condition thresholds (e.g., age limits, passing grades).

### 11. Cumulative Reduction (`_20reduce.py`)

- **Key Concepts:** Rolling computation using `functools.reduce()` to condense iterables down to a single value.
- **Use Cases:** Cumulative summation, computing factorials, and sequential product evaluation.

### 12. Element Pairing (`_21zip.py`)

- **Key Concepts:** Connecting multiple iterables pairwise into tuples.
- **Use Cases:** Combining parallel lists into unified lists of tuples or mapping them directly into key-value dictionaries.

### 13. Index Tracking (`_22enumerate.py`)

- **Key Concepts:** Adding an automatic counter/index to any iterable sequence.
- **Features Covered:** Custom starting indices, character indexing in strings, and structured list loops.

### 14. Randomness & Simulation (`_23random.py`)

- **Key Concepts:** Generating pseudo-random numbers and selecting items randomly.
- **Features Covered:** `randint()`, `choice()`, `choices()`, `sample()`, `shuffle()`, and reproducible sequences via `random.seed()`.
- **Project Demonstration:** Interactive CLI Rock-Paper-Scissors game.

### 15. Mathematics Module (`_24math.py`)

- **Key Concepts:** Standard numerical, rounding, algebraic, and trigonometric operations.
- **Features Covered:** `sqrt()`, `pow()`, `ceil()`, `floor()`, `fabs()`, `gcd()`, `lcm()`, trigonometric angle conversions (`radians`, `degrees`), and mathematical constants (`pi`, `e`).

### 16. Exception Handling (`_25exception.py`)

- **Key Concepts:** Preventing program crashes by handling runtime errors gracefully.
- **Features Covered:** Catching standard exceptions (`ValueError`, `ZeroDivisionError`), implementing multiple `except` blocks, and utilizing the `else` clause for error-free executions.

### 17. File Handling (`_26file_handling.py`)

- **Key Concepts:** Creating, reading, writing, appending, and updating external text files.
- **File Modes Covered:** Read (`r`), Overwrite (`w`), Append (`a`), and Create (`x`).
- **Best Practices:** Context management using `with open()` for auto-closing files and interactive persistent file storage loops (e.g., student registry system).

### 18. Modules & Code Reusability (`_27modules.py`)

- **Key Concepts:** Modularizing code into clean, imported user-defined modules.
- **User-Defined Modules Included:**
  - `calculator.py`: Basic mathematical helper functions (`addition`, `subtract`, `multiply`).
  - `student.py`: Academic helper utilities (`student_info`, `calculate_average`, `check_result`).
- **Module Types Covered:** Built-in/Standard Library, User-defined modules, and Third-party packages.

### 19. Python Decorators (`_28decorator.py`)

- **Key Concepts:** Modifying or enhancing the behavior of existing functions dynamically without altering their core source code.
- **Prerequisites Covered:** Treating functions as first-class objects, assigning functions to variables, passing functions as parameters, nested inner functions, and returning functions.
- **Syntax Covered:** Wrapper functions and explicit syntactic sugar using `@decorator_name`.

### 20. List Comprehension (`_29list_comprehension.py`)

- **Key Concepts:** Concise syntax for creating new lists based on existing iterables with minimal boilerplate.
- **Features Covered:** Standard list expressions, filtering items using `if` conditions, and inline transformations using `if-else` ternary operations.

### 21. Dictionary Comprehension (`_30dict_comprehension.py`)

- **Key Concepts:** Generating dictionaries dynamically using expressions mapped over iterable key-value pairs.
- **Features Covered:** Key-value calculations, conditional key filtering (`if`), inline ternary mapping (`if-else`), and external function integration for complex value processing.
