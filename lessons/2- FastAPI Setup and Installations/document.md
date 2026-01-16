# Lesson 02: FastAPI Setup and Installations

## Introduction

In this lesson, we will set up our development environment.  
Getting the cleanup and setup right is **critical** for a smooth development interaction.

---

## What You Will Learn in This Lesson

By the end of this lesson, you will be able to:

- Create a **Python Virtual Environment**
- Activate the Virtual Environment
- Install **FastAPI** and its dependencies

---

## 2.1 Python Virtual Environment 🐍

### What is a Virtual Environment?

A **Virtual Environment** is a self-contained directory that contains a Python installation for a specific project.

**Why use it?**
- It keeps dependencies required by different projects separate.
- It prevents conflicts between system-wide packages and project-specific packages.
- It is the standard best practice for Python development.

### Creating a Virtual Environment

To create a virtual environment, open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
python -m venv venv
```

This command creates a folder named `venv` in your current directory.

### Activating the Virtual Environment

Before installing any packages, you must **activate** the environment.

#### 🪟 Windows (Command Prompt / PowerShell)

```powershell
.\venv\Scripts\activate
```

> **Note:** If you see an error about scripts being disabled on Windows, you might need to run PowerShell as Administrator and run: `Set-ExecutionPolicy RemoteSigned`.

#### 🍎 macOS / 🐧 Linux

```bash
source venv/bin/activate
```

**How do you know it's activated?**  
You should see `(venv)` appear at the beginning of your terminal prompt.

---

## 2.2 FastAPI and Virtual Environment Installation 📦

Now that our virtual environment is active, we can install FastAPI.

### Installing FastAPI

We will install FastAPI along with the standard dependencies (like `uvicorn` for the server) using `pip`.

Run the following command:

```bash
pip install "fastapi[standard]"
```

> The `[standard]` option installs FastAPI along with the `uvicorn` server coverage and other recommended tools.

### Verifying Installation

To check if everything was installed correctly, you can list the installed packages:

```bash
pip list
```

You should see `fastapi`, `uvicorn`, `pydantic`, `starlette` and others in the list.

### Saving Dependencies

It is good practice to save your project's dependencies to a file.

```bash
pip freeze > requirements.txt
```

---

## Summary ✅

In this lesson, we:
1. Created a Python Virtual Environment (`venv`).
2. Activated the environment.
3. Installed FastAPI using `pip`.

Your environment is now ready for coding!

---

## Next Lesson 🚀

➡️ **Lesson 03: Creating Your First API**
