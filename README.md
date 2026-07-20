# STEM Quiz and Feedback System

A monolithic STEM learning platform that serves a React/TypeScript/Tailwind single-page app and a Django REST API from one Django deployment. It supports session authentication, role-based access, quiz attempts with immediate feedback, score history, and performance reports.

## Structure

- `backend/` — Django + Django REST Framework application, API routes, database models, and static/template serving for the compiled frontend.
- `frontend/` — React + TypeScript source built by Vite into `frontend/dist`, which Django serves at runtime.

## Quick start

Install backend dependencies and prepare the database:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
```

Build the frontend assets:

```bash
cd ../frontend
npm install
npm run build
```

Run the monolith from Django:

```bash
cd ../backend
python manage.py runserver
```

Open `http://localhost:8000`. The React app uses same-origin API calls under `/api`, so no separate frontend server is required for normal use.

## Development mode

You can still run Vite separately for hot-module reloading:

```bash
cd frontend
npm run dev
```

When using the Vite dev server, set `VITE_API_URL=http://localhost:8000/api` if Django is running on port 8000.

## Demo coverage

The codebase includes modular Django apps for authentication, students, subjects, quizzes, reports, and dashboard analytics. The frontend includes landing, auth, student dashboard, subjects, quiz-taking, results, score history, reports, and admin management screens with responsive layouts and dark-mode styling.
