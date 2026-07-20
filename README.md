# STEM Quiz and Feedback System

A production-minded full-stack STEM learning platform with a Django REST backend and a React/TypeScript/Tailwind frontend. It supports session authentication, role-based access, quiz attempts with immediate feedback, score history, and performance reports.

## Structure

- `backend/` — Django + Django REST Framework API using SQLite by default.
- `frontend/` — React + TypeScript SPA using Vite, Tailwind CSS, React Router, React Hook Form, Framer Motion, Axios, Toastify, Lucide icons, and Recharts.

## Quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend expects the API at `http://localhost:8000/api` unless `VITE_API_URL` is set.

## Demo coverage

The codebase includes modular Django apps for authentication, students, subjects, quizzes, reports, and dashboard analytics. The frontend includes landing, auth, student dashboard, subjects, quiz-taking, results, score history, reports, and admin management screens with responsive layouts and dark-mode styling.
