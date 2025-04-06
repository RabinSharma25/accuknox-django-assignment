
# Accuknox Django Trainee Assignment

This repository contains solutions to the assignment provided for the Django Trainee position at **Accuknox**. It covers two major topics:

1. **Django Signals**
2. **Custom Classes in Python**

---

## 🧠 Assignment 1: Django Signals

📁 Directory: `django_signals_assignment/`

This section addresses the following questions:

### ✅ Question 1:
**Are Django signals executed synchronously or asynchronously by default?**  
Includes a code snippet that demonstrates the behavior.

### ✅ Question 2:
**Do Django signals run in the same thread as the caller?**  
Includes a working example showing signal and caller thread info.

### ✅ Question 3:
**Do Django signals run in the same database transaction as the caller?**  
A sample is provided to observe signal execution within a transaction.

📌 To test these, go to the `django_signals_assignment` directory and follow the setup instructions inside the project.

---

## 🧠 Assignment 2: Custom Classes in Python

📁 Directory: `rectangle_class_assignment/`

### Task Description:
Create a `Rectangle` class that:

- Is initialized with `length: int` and `width: int`.
- Is iterable using a `for` loop.
- Yields:
  ```python
  {'length': <value>}
  {'width': <value>}
