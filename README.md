
# Homogeneous System Solver (Ax = 0)

This project implements a basic linear algebra algorithm from scratch to solve the **homogeneous system of linear equations** `Ax = 0`. The solution is expressed in **parametric vector form** using **Reduced Row Echelon Form (RREF)**.

> ❗ No external libraries (like NumPy or SymPy) are used — logic is built purely using core Python, as expected in academic settings or interviews with MathWorks and similar firms.

---

## 📌 Features

- Accepts input matrix `A` from a text file
- Reduces matrix to RREF using:
  - Row exchanges
  - Row scaling
  - Row replacement
- Extracts pivot columns
- Prints the general solution in parametric vector form

---

## 📂 Project Structure

```bash
homogeneous-system-solver/
├── inpMATHassgn.txt      # Input matrix (editable)
├── solver.py             # Main solution code
├── README.md
````

---

## 📥 Input Format

File: `inpMATHassgn.txt`

```
<number_of_rows>
<number_of_columns>
<row_1>
<row_2>
...
<row_n>
```

**Example:**

```
3
5
1 2 1 -1 2
2 4 0 2 6
3 6 1 1 8
```

---

## 🚀 Run Instructions

```bash
cd Homogeneous-System-Solver
python solver.py
```

The script reads `inpMATHassgn.txt`, prints:

* Pivot positions
* RREF
* General solution in parametric vector form

---

## 🔍 Sample Output

```
PIVOT POSITION:
[(0, 0), (1, 2)]
RREF:
1.0  2.0  0.0  0.0  1.0
0.0  0.0  1.0  1.0  2.0
0.0  0.0  0.0  0.0  0.0

SOLUTION:
[0, 0, 0, 0, 0]+x_2*[-2.0, 1, 0.0, 0.0, 0.0]+x_4*[0.0, 0.0, -1.0, 1, 0.0]+x_5*[-1.0, 0.0, -2.0, 0.0, 1]
```

---

## 📘 Concepts Used

* Elementary Row Operations (as taught in Linear Algebra courses)
* Gaussian Elimination to RREF
* Parametric solution form

---

## 📄 License

MIT License
