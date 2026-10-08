# Student Record Management API

A RESTful Student Record Management API built using **Django** and **Django REST Framework (DRF)**.

This project was developed as part of the **CodSoft Backend Development Internship – Task 1**. The API manages students, courses, and enrollments with CRUD operations, validation, searching, filtering, sorting, and pagination.


## 📌 Task Overview

The objective of this task is to build a backend system that manages:

- Students
- Courses
- Student Enrollments

The API provides complete CRUD functionality along with data validation, search, filtering, sorting, pagination, and appropriate HTTP responses.


## 🚀 Features

### Student Management

- Create a new student
- Retrieve all students
- Retrieve a single student
- Update student information
- Partially update student information
- Delete a student
- Email uniqueness validation
- Indian phone number validation
- Age validation
- Search students
- Filter students
- Sort students
- Pagination

### Course Management

- Create a new course
- Retrieve all courses
- Retrieve a single course
- Update course information
- Partially update course information
- Delete a course
- Unique course code validation
- Course duration management
- Course fee management
- Search courses
- Filter courses
- Sort courses
- Pagination

### Enrollment Management

- Create enrollment
- Retrieve all enrollments
- Retrieve a single enrollment
- Update enrollment
- Partially update enrollment
- Delete enrollment
- Student-Course relationship
- Enrollment status management
- Duplicate enrollment validation
- Search enrollments
- Filter enrollments
- Sort enrollments
- Pagination

---

# 🛠️ Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **django-filter**
- **SQLite**
- **python-dotenv**
- **Git**
- **GitHub**
- **Postman** for API testing


# 🔗 API Endpoint Summary

| Resource          | Method | Endpoint                 |
| ----------------- | ------ | ------------------------ |
| Students          | GET    | `/api/students/`         |
| Students          | POST   | `/api/students/`         |
| Student Detail    | GET    | `/api/students/{id}/`    |
| Student Detail    | PUT    | `/api/students/{id}/`    |
| Student Detail    | PATCH  | `/api/students/{id}/`    |
| Student Detail    | DELETE | `/api/students/{id}/`    |
| Courses           | GET    | `/api/courses/`          |
| Courses           | POST   | `/api/courses/`          |
| Course Detail     | GET    | `/api/courses/{id}/`     |
| Course Detail     | PUT    | `/api/courses/{id}/`     |
| Course Detail     | PATCH  | `/api/courses/{id}/`     |
| Course Detail     | DELETE | `/api/courses/{id}/`     |
| Enrollments       | GET    | `/api/enrollments/`      |
| Enrollments       | POST   | `/api/enrollments/`      |
| Enrollment Detail | GET    | `/api/enrollments/{id}/` |
| Enrollment Detail | PUT    | `/api/enrollments/{id}/` |
| Enrollment Detail | PATCH  | `/api/enrollments/{id}/` |
| Enrollment Detail | DELETE | `/api/enrollments/{id}/` |


# 📁 Project Structure


studentrecord/
│
├── student/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── paginations.py
│
├── course/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── paginations.py
│
├── enrollment/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── paginations.py
│
├── studentrecord/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
