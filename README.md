# 🐍 Python Internship Preparation Program

> A structured 4-week roadmap to go from Python basics to internship-ready — covering foundations, OOP, data libraries, scikit-learn, and interview prep.

---

## 📁 Repository Structure

```
python-internship-prep/
│
├── week1-foundations/
│   ├── practice_questions.py
│   └── mini_project/
│       └── contact_book_cli.py
│
├── week2-intermediate/
│   ├── practice_questions.py
│   └── mini_project/
│       └── library_management.py
│
├── week3-data-libraries/
│   ├── eda_notebook.ipynb
│   └── mini_project/
│       └── titanic_eda.ipynb
│
├── week4-interview-prep/
│   ├── dsa_practice.py
│   └── leetcode_solutions/
│
├── student-performance-predictor/   ← Capstone Project
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   │   ├── student.py
│   │   ├── data_loader.py
│   │   └── model.py
│   └── README.md
│
└── README.md
```

---

## 📅 4-Week Roadmap

### Week 1 — Python Foundations

| Topic | Concepts |
|-------|----------|
| Syntax & Strings | Variables, data types, string methods, type casting |
| Control Flow | if/elif/else, for/while loops, break/continue/pass |
| Data Structures | Lists, Tuples, Sets, Dictionaries, list comprehensions |
| Functions | def, return, scope, *args/**kwargs, lambda, map/filter |

**Practice Questions (12 total)**

1. Reverse a string without using `[::-1]`
2. Count vowels in a sentence
3. Check if a string is a palindrome
4. Print multiplication table of any number
5. Find all prime numbers between 1–100
6. Print Fibonacci series up to n terms
7. Remove duplicates from a list without `set()`
8. Merge two dictionaries and sort by value
9. Find the second largest number in a list
10. Factorial using recursion
11. Lambda to filter even numbers from a list
12. Use `map()` to square all numbers in a list

**Mini Project:** Calculator CLI App + Number Guessing Game

---

### Week 2 — Intermediate Python

| Topic | Concepts |
|-------|----------|
| OOP | Classes, objects, `__init__`, inheritance, polymorphism, dunder methods |
| File Handling | open/read/write, context managers, CSV, JSON, os/shutil |
| Error Handling | try/except/finally, custom exceptions, raise, debugging |
| Key Modules | math, random, datetime, collections, itertools, re (regex) |

**Practice Questions (12 total)**

1. `BankAccount` class with deposit, withdraw, balance check
2. `SavingsAccount` extending `BankAccount` with interest calculation
3. `__str__` and `__repr__` in a `Student` class
4. Read a `.txt` file and count word frequency
5. Save/load a contacts list to/from JSON
6. Copy file content, skipping blank lines
7. Handle `ZeroDivisionError`, `ValueError`, `TypeError` in a calculator
8. Create custom `AgeNotValidError` exception
9. Use `finally` to always close a file
10. Use `collections.Counter` for most common word
11. Generate a 6-digit OTP using `random`
12. Use `datetime` to count days until New Year

**Mini Project:** Student Grade Manager (OOP + File I/O)

---

### Week 3 — Data & Libraries

| Library | Key Topics |
|---------|------------|
| NumPy | Arrays, indexing, broadcasting, statistical functions |
| Pandas | Series/DataFrame, read_csv, groupby, merge, missing data |
| Matplotlib & Seaborn | Line/bar/scatter, heatmaps, histograms, subplots |
| Requests & APIs | HTTP GET/POST, REST APIs, JSON parsing, BeautifulSoup basics |

**Mini Project:** EDA on a real dataset (Titanic / IPL / Sales)

---

### Week 4 — Interview Prep & Coding Practice

| Area | Focus |
|------|-------|
| DSA in Python | Arrays, strings, hashing, stacks, queues, recursion, sorting |
| LeetCode | 5 Easy/day (days 1–3), mix Easy + Medium (days 4–5) |
| Interview Topics | Python-specific Q&A, OOP questions, Big O complexity |
| Portfolio & GitHub | Clean READMEs, GitHub push, LinkedIn/resume update |

**Capstone Project:** Weather Dashboard CLI / To-Do API / Data Analysis Report

---

## 🚀 Capstone Project — Student Performance Predictor

**One project covering all 4 weeks:**

| Week | Concepts Used | How It's Used |
|------|--------------|---------------|
| Week 1 | Syntax, loops, functions | Data cleaning functions, input handling |
| Week 2 | OOP, file I/O, error handling | `Student` class, CSV load/save, try/except |
| Week 3 | Pandas, NumPy, Matplotlib, Seaborn | EDA, visualize score distributions |
| Week 4 | Scikit-learn | Train Logistic Regression / Decision Tree model |

**Dataset:** [Student Performance Dataset — Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

**What it does:**
- Takes student data: study hours, attendance, past scores
- Cleans & analyzes data with Pandas
- Visualizes trends with Matplotlib & Seaborn
- Predicts student pass/fail using scikit-learn

**Tech Stack:** Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn

---

## ⚙️ Setup & Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/python-internship-prep.git
cd python-internship-prep

# Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install numpy pandas matplotlib seaborn scikit-learn requests beautifulsoup4 jupyter
```

---

## 📚 Resources

| Resource | Link |
|----------|------|
| Official Python Docs | https://docs.python.org/3/ |
| freeCodeCamp Python | https://www.freecodecamp.org |
| LeetCode (DSA practice) | https://leetcode.com |
| Kaggle Datasets | https://www.kaggle.com/datasets |
| Scikit-learn Docs | https://scikit-learn.org/stable/ |
| Replit (online IDE) | https://replit.com |

---

## ⚡ Daily Tips

- ⏰ Study **2–3 hours/day** consistently — weekends too
- ✍️ **Code every single day** — no passive watching
- 🧪 **Build something** after every topic you finish
- 📝 Keep a **notebook of errors + solutions**
- 🔗 Push everything to **GitHub daily**
- 🤝 Join **Python Discord / Reddit** communities

---

## 📈 Progress Tracker

- [ ] Week 1 — Foundations complete
- [ ] Week 2 — Intermediate complete
- [ ] Week 3 — Data & Libraries complete
- [ ] Week 4 — Interview Prep complete
- [ ] Capstone Project deployed on GitHub

---

## 👨‍💻 Author

Built for Python internship preparation · 30 days · 4 weeks · 1 goal 🐍

> *"Code every day. Push to GitHub. Land the internship."*
