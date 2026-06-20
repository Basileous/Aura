# Aura — Django E‑commerce Demo

A lightweight, deployable e‑commerce web application built with Django. Features product catalog, image uploads, shopping cart, checkout, user accounts, order history and admin management.

**Quick Start**

- **Prerequisites:** Python 3.9+, pip, virtualenv (recommended).
- Create and activate a virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Install dependencies:

```powershell
pip install -r requirements.txt
```

- Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

- Run the development server:

```powershell
python manage.py runserver
```

**Project Structure (high level)**

- `ecommerce_website_django/` — Django project (settings, wsgi/asgi, urls)
- `App_Shop/`, `App_Order/`, `App_Payment/`, `App_Login/` — application modules
- `templates/`, `static/`, `media/` — frontend assets and uploaded media
- `scratch/` — helper scripts for seeding data

**Deployment (Vercel)**

- This repo includes a `vercel.json` configured to route to `ecommerce_website_django/wsgi.py` and a top-level `requirements.txt` for dependency installation.
- On Vercel, set the environment variables: `SECRET_KEY`, `DEBUG=false`, any database or email credentials, and configure a production database instead of SQLite.

**Notes & Tips**

- The repo uses `django-crispy-forms`, `crispy-bootstrap4`, `django-cleanup` and `Pillow` for image handling.
- Run `pip freeze > requirements.txt` locally to capture exact pinned versions before deployment.
- Media files are stored under the `media/Products` folder — configure persistent storage for production (S3, etc.).

**Security**

- If you accidentally exposed any tokens or secrets, revoke them immediately and rotate credentials.

**Useful Commands**

```powershell
# install deps
pip install -r requirements.txt
# run migrations
python manage.py migrate
# seed sample data (if using scripts)
python scratch/seed_products.py
```

---
Maintainer: Basil Joseph
License: MIT

