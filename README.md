# 🧠 Productivity Tracker (FastAPI Backend)

## 📌 Overview

This project is a task management backend system built using FastAPI.  
It was initially developed as a CLI application and later evolved into a RESTful API with proper request handling, validation, and database integration.

The system demonstrates core backend concepts such as API design, layered architecture, and database operations.

---

## 🚀 Features

- Create, update, and delete tasks (CRUD)
- Mark tasks as completed
- Filter tasks by priority and status
- Sort tasks by due date and priority (custom logic)
- Task statistics (total, completed, pending)
- Structured request/response handling using Pydantic
- Persistent storage using SQLite
- Proper HTTP status codes and error handling

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- SQLite

---

## 📂 Project Structure
task-manager-api/
│── api.py # API layer (routes & request handling)
│── task_manager.py # Business logic layer
│── database.py # Database operations (SQL queries)
│── README.md


---

## ⚙️ How to Run

### Install Dependencies
pip install fastapi uvicorn

### Run Server

uvicorn api:app --reload


### Access API Docs

Open in browser:


http://127.0.0.1:8000/docs


---

## 📡 API Endpoints

### Core CRUD

- POST /tasks → Create a new task  
- GET /tasks → Get all tasks  
- PUT /tasks/{task_id} → Update task status  
- DELETE /tasks/{task_id} → Delete task  

### Advanced Features

- PATCH /tasks/{task_id}/name → Update task name  
- GET /tasks/filter → Filter tasks  
- GET /tasks/sort → Sort tasks  
- GET /tasks/stats → Get task statistics  

---

## 🧠 Key Learnings

- Designed a RESTful API using FastAPI
- Implemented layered architecture (API → Logic → Database)
- Used Pydantic for request validation and structured responses
- Integrated SQLite for persistent storage
- Handled errors using HTTPException and proper status codes
- Implemented filtering and sorting using SQL queries
- Prevented SQL injection using parameterized queries and validation

---

## ⚠️ Limitations

- SQLite is not ideal for high concurrency systems
- No authentication (single-user system)
- No pagination for large datasets

---

## 🚀 Future Improvements

- Add authentication (JWT)
- Migrate to PostgreSQL
- Add pagination
- Add caching
- Deploy to cloud (Render / AWS)

---

## 🎯 Summary

This project demonstrates backend fundamentals such as API design, validation, database integration, and clean architecture.  
It reflects the ability to build and structure a complete backend system.

