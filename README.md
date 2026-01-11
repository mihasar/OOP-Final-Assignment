# OOP Final Assignment - 2026

**Student Name:** Michael Saravaisky
**ID:** 211460605
**Course:** Object Oriented Programming (OOP)
**Submission Date:** 10/01/2026

---

## 📌 Overview
This repository contains the solutions for the OOP final practice assignment.
 The solutions demonstrate core OOP principles including **Encapsulation**, **Polymorphism**, and **MVC Architecture**.

## 📂 Project Structure

### 1. Encapsulation (Section 1)
* **File:** `q1_invoice.py`
* **Description:** An `Invoice` class implementation using private attributes protected by `@property` decorators and validation logic.

### 2. Polymorphism (Section 3)
* **File:** `q3_polymorphism.py`
* **Description:** Demonstration of:
    * **Duck Typing** (Part A)
    * **Abstract Base Classes (ABC)** & Inheritance (Part C)
    * Runtime type checking using `isinstance`.

### 3. MVC Architecture (Section 5)
A "Person Management" system implementing the **Model-View-Controller** design pattern.

* **Files:**
    * `main.py`: Entry point for the application.
    * `controller.py`: Manages the flow between View and Model.
    * `model.py`: Manages data and logic (creates and stores `Person` objects).
    * `view.py`: Handles user input and output (CLI).
    * `Person.py`: A Data Class representing a person entity.

---

## 🚀 How to Run

Ensure you have Python installed. You can run each section independently via the terminal:

**Run Invoice System (Q1):**
```bash
python q1_invoice.py