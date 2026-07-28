<div align="center">

# 🐍 Ultimate Python Programming Masterclass

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Learning-brightgreen?style=for-the-badge&logo=github)
![Author](https://img.shields.io/badge/Author-Aniket_Singh-FF6F61?style=for-the-badge&logo=person&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

<p align="center">
  <b>A comprehensive, hands-on, chapter-wise guide to mastering Python from absolute basics to Object-Oriented Programming and mini-projects!</b>
</p>

---

[🚀 Getting Started](#-getting-started) •
[📚 Chapter Breakdown](#-chapter-wise-learning-path) •
[🎮 Mini Projects](#-mini-projects-built) •
[📁 Repository Tree](#-repository-structure) •
[💻 How to Run](#-how-to-run)

---

</div>

## 🌟 Overview

Welcome to the **Python Chapterwise Learning Repository**! This repository is carefully structured to take learners through the core concepts of Python step-by-step. Each chapter contains detailed code explanations, practical problem-solving tasks, real-world examples, and fun interactive projects.

```
       ┌─────────────────────────────────────────────────────────┐
       │   🐍 Python Core Syntax  ──►  📊 Data Structures       │
       │           │                            │                │
       │           ▼                            ▼                │
       │   🔁 Control Flow        ──►  ⚙️  Functions & File I/O │
       │           │                            │                │
       │           ▼                            ▼                │
       │   🧩 Object Oriented (OOP)──► 🎮 Interactive Projects │
       └─────────────────────────────────────────────────────────┘
```

---

## 📚 Chapter-Wise Learning Path

| Chapter | Topic | Key Concepts Covered | Practice Problems |
| :--- | :--- | :--- | :---: |
| 📄 [ch-1.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-1.py) | **Python Basics & Modules** | `pyjokes`, `pyttsx3` text-to-speech, multi-line printing (`'''`) | 2 |
| 📄 [ch-2.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-2.py) | **Variables & Datatypes** | Type casting (`int()`, `float()`), Arithmetic, Logical (`&`, `|`, `not`), User `input()` | 3 |
| 📄 [ch-3.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-3.py) | **String Manipulation** | Slicing `[start:stop:step]`, Negative indexing, `f-strings`, `.replace()`, `.find()` | 3 |
| 📄 [ch-4.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-4.py) | **Lists & Tuples** | Mutable vs Immutable, `.append()`, `.sort()`, `.pop()`, `.count()`, `.index()`, `sum()` | 3 |
| 📄 [ch-5.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-5.py) | **Dictionaries & Sets** | Key-Value pairs, `.keys()`, `.values()`, `.update()`, Unique Sets, `.union()`, `.intersection()` | 4 |
| 📄 [ch-6.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-6.py) | **Conditional Logic** | `if-elif-else` branches, Spam filter, Length checks, Member testing (`in`) | 6 |
| 📄 [ch-7.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-7.py) | **Loops & Iteration** | `while` loops, `for` in `range()`, `break`, `continue`, Prime checker, Star patterns | 9 |
| 📄 [ch-8.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-8.py) | **Functions & Recursion** | Parameters, Returns, Recursive factorials, Temperature Converter, Sum of N numbers | 3 |
| 📄 [ch-9.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-9.py) | **File I/O Operations** | `open()`, `read()`, `write()`, `with` context manager, Word censorship, Auto table generator | 3 |
| 📄 [ch-10.py](file:///d:/My%20Apps/languages/Python/python%20code/ch-10.py) | **Object-Oriented Programming** | Classes, Objects, `self`, `@staticmethod`, `__init__` constructor, Train Booking | 3 |
| 📄 [OOPS.PY](file:///d:/My%20Apps/languages/Python/python%20code/OOPS.PY) | **OOP Concepts** | Encapsulation demo, Car Class implementation | 1 |
| 📄 [extra.py](file:///d:/My%20Apps/languages/Python/python%20code/extra.py) | **Built-in Utilities** | Print parameters (`sep`, `end`), `max()`, `min()` helpers | 2 |

---

## 🎮 Mini Projects Built

<div align="center">

### 1️⃣ 🪨 📄 ✂️ Rock Paper Scissors Game
**File:** [`proj1.py`](file:///d:/My%20Apps/languages/Python/python%20code/proj1.py)

Play against an AI computer opponent! Built using Python's `random` module with win/loss/draw detection and infinite replay mode.

```bash
Enter a choice (Rock: r, Paper: p, Scissor: s) or 'q' to quit: r
YOU WIN!! Computer chose: s, you chose: r
```

---

### 2️⃣ 🎯 Number Guessing Game
**File:** [`proj2.py`](file:///d:/My%20Apps/languages/Python/python%20code/proj2.py)

An interactive guessing game where the computer picks a random number from 1–100 and gives hint feedback (*"choose a bigger number"* / *"choose a smaller number"*) while tracking total attempts.

```bash
Guess a number between 1 and 100: 50
choose a bigger number
Guess a number between 1 and 100: 75
You Guess the number 75 in 2 attempts
```

---

### 3️⃣ 📐 Geometry & Time Calculators
**File:** [`proj.py`](file:///d:/My%20Apps/languages/Python/python%20code/proj.py)

Console utility script for quick mathematical conversions:
- 🟦 Rectangle Area & Perimeter
- 🟢 Circle Area & Perimeter
- ⏰ Hours + Minutes + Seconds to Total Seconds Converter

</div>

---

## 📁 Repository Structure

```directory
python code/
├── 📄 README.md              # Project Documentation
├── 📄 ch-1.py                # Python Intro & Modules
├── 📄 ch-2.py                # Data Types & Operators
├── 📄 ch-3.py                # String Slicing & Formatting
├── 📄 ch-4.py                # Lists & Tuples Data Structures
├── 📄 ch-5.py                # Dictionaries & Sets
├── 📄 ch-6.py                # Conditional Logic Statements
├── 📄 ch-7.py                # Loops, Iteration & Star Patterns
├── 📄 ch-8.py                # Functions & Recursion
├── 📄 ch-9.py                # File I/O & Automation
├── 📄 ch-10.py               # OOP Classes, Methods & System
├── 📄 OOPS.PY                # Encapsulation & OOP Demo
├── 📄 extra.py               # Extra Print & Built-in functions
├── 📄 proj.py                # Math & Time Calculator
├── 📄 proj1.py               # Rock Paper Scissors Game
├── 📄 proj2.py               # Number Guessing Game
└── 📁 tables/                # Auto-generated multiplication files
```

---

## 💡 Code Highlights

### ⚡ Automatic Table File Generator (File I/O)
Generate multiplication tables for numbers 2 to 27 automatically in text files!

```python
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 28):
    generateTable(i)
```

---

### 🚆 Object-Oriented Train Reservation System
Demonstrating clean Class structure with methods and parameters:

```python
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket booked on Train #{self.trainNo} from {fro} to {to}")

    def getFare(self, fro, to):
        print(f"Fare checking for Train #{self.trainNo} from {fro} to {to}")

t = Train(2456)
t.book("Delhi", "Mumbai")
```

---

## 💻 How to Run

### Prerequisites
Make sure Python 3.x is installed on your system.

```bash
# Check Python version
python --version
```

### Optional External Packages
Some early chapters utilize external modules (`pyjokes` and `pyttsx3`):

```bash
pip install pyjokes pyttsx3
```

### Run Any Chapter or Project
Execute any `.py` script directly using python:

```bash
# Run Chapter 1
python ch-1.py

# Run Rock Paper Scissors Project
python proj1.py

# Run Number Guessing Game
python proj2.py
```

---

<div align="center">

### 🎨 Crafted with ❤️ by [Aniket Singh](https://github.com/Aniketsingh-45)

⭐ **If you find this repository helpful, don't forget to give it a star!** ⭐

</div>
