# 🧠 Productivity Tracker (CLI → FastAPI Backend)

## 📌 Overview

This project is a task management system that was initially built as a command-line application and later upgraded into a FastAPI-based REST API.

The upgrade introduced structured request handling, validation, and the ability to interact with the system over HTTP, making it more scalable and closer to real-world backend applications.

---

## 🚀 Features

* Add, edit, and delete tasks
* Mark tasks as completed
* Search tasks by name
* Filter tasks by priority (high, medium, low)
* Sort tasks by due date and priority
* Structured request and response handling using Pydantic
* Persistent storage using JSON
* RESTful API design with CRUD operations

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic
* JSON (for storage)

---

## 📂 Project Structure

```text
productivitytracker/
│── main.py          # CLI interface
│── api.py           # FastAPI routes (API layer)
│── task_manager.py  # Business logic
│── storage.py       # JSON load/save operations
│── tasks.json       # Data storage
```

---

## ⚙️ How to Run

### 🔹 Run CLI Version


python main.py

### 🔹 Run API Version

uvicorn api:app --reload

### 🔹 Access API Docs

http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

* **POST /tasks** → Create a new task
* **GET /tasks** → Get all tasks
* **PUT /tasks/{index}** → Mark a task as completed
* **DELETE /tasks/{index}** → Delete a task

---

## 🧠 Key Learnings

* Converted a CLI application into a RESTful API
* Understood how FastAPI maps routes to handler functions
* Learned how Pydantic models validate and structure data
* Implemented request body handling using JSON
* Designed clean API responses with response models
* Handled validation errors and debugging effectively
* Separated API layer from business logic for better structure

---

## ⚠️ Limitations

* Uses JSON file instead of a database
* Not suitable for concurrent users (race conditions possible)
* Uses index instead of unique identifiers

---

## 🚀 Future Improvements

* Replace JSON storage with SQLite/PostgreSQL
* Add authentication (JWT)
* Use UUID instead of index-based operations
* Deploy the API to cloud platforms

---

## 🎯 Summary

This project demonstrates backend fundamentals such as API design, validation, routing, and data persistence, and serves as a strong foundation for building scalable systems.
