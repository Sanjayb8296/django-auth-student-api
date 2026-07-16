# Setup & Run Guide

Step-by-step instructions to run **django-auth-student-api** locally.

---

## 1. Prerequisites

- **Python 3.10 or newer** — check with:
  ```bash
  python --version
  ```
- **pip** (comes with Python) and **git**.

---

## 2. Get the code

```bash
git clone https://github.com/Sanjayb8296/django-auth-student-api.git
cd django-auth-student-api
```

> If you downloaded a ZIP instead, just unzip it and `cd` into the folder.

---

## 3. Create & activate a virtual environment

A virtual environment keeps this project's packages separate from your system.

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
> If PowerShell blocks the script, run once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Windows (cmd):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You'll know it worked when your prompt shows `(.venv)`.

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Set up the database

The app uses SQLite (a file, `db.sqlite3`). Create the tables:

```bash
python manage.py migrate
```

---

## 6. (Optional) Create an admin user

To use the Django admin at `/admin/`:

```bash
python manage.py createsuperuser
```
Follow the prompts for username / email / password.

---

## 7. Run the development server

```bash
python manage.py runserver
```

Open your browser to:

- App / login page → <http://127.0.0.1:8000/>
- Dashboard (after login) → <http://127.0.0.1:8000/dashboard/>
- Admin → <http://127.0.0.1:8000/admin/>

Press **Ctrl + C** to stop the server.

---

## 8. Try the API

You can register a user and create students with `curl` (or Postman).

**Register a new user:**
```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"prashant\", \"password\": \"secret123\"}"
```

**Log in:**
```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"prashant\", \"password\": \"secret123\"}"
```

**Create a student:**
```bash
curl -X POST http://127.0.0.1:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"Asha\", \"age\": 21, \"email\": \"asha@example.com\", \"course\": \"CS\"}"
```

**List all students:**
```bash
curl http://127.0.0.1:8000/api/students/
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `python: command not found` | Try `python3` instead, or install Python from python.org. |
| `.venv\Scripts\Activate.ps1 cannot be loaded` | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then retry. |
| `no such table` errors | You skipped step 5 — run `python manage.py migrate`. |
| Port 8000 already in use | Run on another port: `python manage.py runserver 8001`. |
| CSRF errors from the browser | Auth endpoints expect Django's CSRF token; call them from the app pages or include the token. |

---

Happy hacking! 🎉
