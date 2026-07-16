# django-auth-student-api

A Django practice project demonstrating **session-based user authentication**
(login, register, logout) and a small **Student management JSON API**, backed
by SQLite. Built while learning Django's built-in `django.contrib.auth`.

> ⚠️ **Learning project.** It uses Django's default development settings
> (`DEBUG = True` and an insecure `SECRET_KEY`). Do **not** deploy as-is.

---

## ✨ Features

- 🔐 **User authentication** using Django's built-in auth system
  (`authenticate`, `login`, `logout`, `create_user` — passwords are hashed).
- 📝 **Register / Login / Logout** JSON API endpoints.
- 🏠 **Login page** and a **login-protected dashboard** (server-rendered HTML).
- 🎓 **Student API** — list and create students (`name`, `age`, `email`, `course`).
- 🗄️ **SQLite** database (zero setup, file-based).

---

## 🧰 Tech stack

| Layer     | Technology            |
|-----------|-----------------------|
| Backend   | Django 5.2            |
| Language  | Python 3.10+          |
| Database  | SQLite                |
| Auth      | Django sessions       |
| Frontend  | Django templates (HTML) |

---

## 📡 API reference

Base URL: `http://127.0.0.1:8000`

### Pages (HTML)

| Method | Path          | Description                                   |
|--------|---------------|-----------------------------------------------|
| GET    | `/`           | Login page (redirects to dashboard if logged in) |
| GET    | `/dashboard/` | Protected dashboard (redirects to `/` if not logged in) |
| GET    | `/admin/`     | Django admin site                             |

### Auth API (JSON)

| Method | Path             | Body                        | Success                     |
|--------|------------------|-----------------------------|-----------------------------|
| POST   | `/api/register/` | `{ "username", "password" }` | `201` — account created & logged in |
| POST   | `/api/login/`    | `{ "username", "password" }` | `200` — welcome message     |
| POST   | `/api/logout/`   | *(none)*                    | `200` — session cleared     |

Errors: `401` invalid credentials, `400` username already taken.

### Student API (JSON)

| Method | Path              | Body                                      | Success                 |
|--------|-------------------|-------------------------------------------|-------------------------|
| GET    | `/api/students/`  | *(none)*                                  | `200` — list of students |
| POST   | `/api/students/`  | `{ "name", "age", "email", "course" }`    | `201` — `{ message, id }` |

---

## 📂 Project structure

```
prashant_practice/
├── manage.py                 # Django CLI entry point
├── requirements.txt          # Python dependencies
├── db.sqlite3                # SQLite database (git-ignored)
├── Login/                    # The main app
│   ├── models.py             # Student model
│   ├── views.py              # Auth + Student views
│   ├── urls.py               # App routes
│   ├── migrations/
│   └── templates/
│       ├── login.html
│       └── dashboard.html
└── prashant_practice/        # Project config
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

## 🚀 Getting started

See **[SETUP.md](SETUP.md)** for full step-by-step instructions.

Quick version:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000>.

---

## 📄 License

Personal learning project — free to use as a reference.
