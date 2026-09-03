# 🧮 Matrix Inverse Calculator

[🇮🇷 فارسی](README.fa.md)

A simple Python project that calculates the **inverse of 2×2 and 3×3 matrices** using the mathematical formulas for determinants, minors, cofactors, and adjugate matrices.

The project is implemented with **Python and NumPy**, without using NumPy's built-in matrix inverse function.

---

## ✨ Features

* 🔢 Calculate the inverse of **2×2 matrices**
* 🔢 Calculate the inverse of **3×3 matrices**
* 📐 Calculate determinants using mathematical formulas
* 🧩 Generate the **Minor Matrix** for 3×3 matrices
* 🔗 Generate the **Cofactor Matrix**
* 🔄 Generate the **Adjugate Matrix**
* ⚠️ Detect singular matrices that do not have an inverse
* 🐍 Simple and beginner-friendly Python implementation

---

## 📁 Project Structure

```text
Matrix-Inverse/
│
├── inverse_2x2.py       # Inverse of a 2×2 matrix
├── inverse_3x3.py       # Inverse of a 3×3 matrix
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 📐 Mathematical Method

### 2×2 Matrix

For a matrix:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

the inverse is calculated as:

$$
A^{-1} =
\frac{1}{ad-bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

The determinant is:

$$
\det(A)=ad-bc
$$

If the determinant is zero, the matrix is **singular** and does not have an inverse.

---

### 3×3 Matrix

For a 3×3 matrix, the program follows these steps:

```text
Matrix
   ↓
Minor Matrix
   ↓
Cofactor Matrix
   ↓
Adjugate Matrix
   ↓
Determinant
   ↓
Inverse Matrix
```

The inverse is calculated using:

$$
A^{-1} = \frac{\mathrm{adj}(A)}{\det(A)}

$$

where:

* **Minor Matrix** contains the minors of the matrix.
* **Cofactor Matrix** applies the appropriate positive and negative signs to the minors.
* **Adjugate Matrix** is the transpose of the cofactor matrix.

---

## 🚀 Installation

Make sure you have **Python 3** installed.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Matrix-Inverse.git
cd Matrix-Inverse
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the desired program:

### 2×2 Matrix

```bash
python inverse_2x2.py
```

Example input:

```text
[[1, 2], [3, 4]]
```

### 3×3 Matrix

```bash
python inverse_3x3.py
```

Example input:

```text
[[1, 2, 3], [0, 1, 4], [5, 6, 0]]
```

The calculated inverse will then be displayed in the terminal.

---

## ⚠️ Singular Matrices

A matrix is **singular** when its determinant is zero:

$$
\det(A)=0
$$

Such a matrix does not have an inverse.

For example:

```text
[[1, 2, 3],
 [2, 4, 6],
 [1, 5, 7]]
```

This matrix is singular because its determinant is zero.

---

## 🛠️ Technologies

* **Python**
* **NumPy**
* **Ast** (`ast.literal_eval`)

---

## 🎯 Purpose

This project was created as a practical exercise to combine **linear algebra** with **Python programming**.

Rather than relying on a built-in matrix inverse function, the calculations are implemented step by step using the underlying mathematical concepts.

---

## 📌 Future Improvements

Possible future improvements include:

* [ ] Support for larger matrices such as **4×4 and N×N**
* [ ] Add a graphical user interface
* [ ] Automatic matrix size detection
* [ ] Cleaner and more modular implementation

---

## 📄 License

This project is open-source and available for learning and educational purposes.
