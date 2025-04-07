# Django Trainee Assignment – Accuknox

This repository contains solutions to the Django Signals and Python Custom Class problems assigned for the Django Trainee position at **Accuknox**. The repository is organized into two directories:

- `django-signals`: Contains Django signal-related examples with proof-of-concept implementations.
- `custom-classes-python`: Contains Python code for a custom `Rectangle` class with iterable behavior.

---

## 📦 Project Setup Instructions

Before running the code examples, make sure your environment is properly configured. Follow the setup instructions below for your operating system:

### 1. Clone the Repository

#### Using HTTPS:
```bash
git clone https://github.com/RabinSharma25/accuknox-django-trainee-assignment.git
cd accuknox-django-trainee-assignment
```

#### Using SSH:
```bash
git clone git@github.com:RabinSharma25/accuknox-django-trainee-assignment.git
cd accuknox-django-trainee-assignment
```

### 2. Install Python and pip

#### For **Windows**:
- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, ensure **Add Python to PATH** is checked.
- Open Command Prompt and verify:
```bash
python3 --version
pip3 --version
```

#### For **macOS**:
```bash
brew install python
python3 --version
pip3 --version
```

#### For **Linux (Ubuntu/Debian)**:
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
pip3 --version
```

### 3. Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
```

### 4. Install Dependencies

All dependencies are listed in the `requirements.txt` file. To install them:

```bash
pip3 install -r requirements.txt
```

---

## 🧹 Topic: Django Signals

**Directory**: [`django-signals`](./django-signals)

**🔧 Run Initial Migrations (Required before execution):**
```bash
cd django-signals
python3 manage.py makemigrations
python3 manage.py migrate
```
---
### ❓ Question 1:
> By default, are Django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**✅ Answer**:  
Django signals are executed **synchronously** by default. When the sender code executes, the connected signal handler runs immediately.

**📂 Code File**: [`01_test_signal_sync.py`](./django-signals/core/01_test_signal_sync.py)

**▶️ Commands to Execute**:
```bash
cd django-signals
python3 core/01_test_signal_sync.py
```

---

### ❓ Question 2:
> Do Django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**✅ Answer**:  
Yes, Django signals run in the **same thread** as the caller. We can confirm this by comparing the `threading.get_ident()` of the sender and the signal.

**📂 Code File**: [`02_test_signal_thread.py`](./django-signals/core/02_test_signal_thread.py)

**▶️ Commands to Execute**:
```bash
cd django-signals
python3 core/02_test_signal_thread.py
```

---

### ❓ Question 3:
> By default, do Django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**✅ Answer**:  
Yes, by default, signals like `post_save` run within the same transaction scope as the caller unless `transaction.on_commit()` is used.

**📂 Code File**: [`03_test_signal_transaction.py`](./django-signals/core/03_test_signal_transaction.py)

**▶️ Commands to Execute**:
```bash
cd django-signals
python3 core/03_test_signal_transaction.py
```

---

## 📆 Topic: Custom Classes in Python

**Directory**: [`custom-classes-python`](./custom-classes-python)

### 🔮 Description:
Create a `Rectangle` class with the following requirements:
1. Accept `length: int` and `width: int` during initialization.
2. Supports iteration.
3. When iterated, yields values in the following format:
   ```python
   {'length': <VALUE>}
   {'width': <VALUE>}
   ```

**📂 Code File**: [`custom-classes-python/rectangle.py`](./custom-classes-python/rectangle.py)

**▶️ Commands to Execute**:
```bash
cd custom-classes-python
python3 main.py
```

---

## 📄 requirements.txt

```txt
Django>=4.0
```

Install via:
```bash
pip3 install -r requirements.txt
```

---

## 📨 Contact

**Rabin**  
📧 your.email@example.com  
👤 [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

