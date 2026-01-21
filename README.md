# Ethara AI | HRMS Portal

A lightweight, professional Human Resource Management System (HRMS) built with Django and PostgreSQL, featuring the sleek Ethara AI branding.

## 🚀 Features

- **Employee Management**: Full CRUD (Create, Read, Update, Delete) functionality for employee records.
- **Attendance Tracking**: Intuitive interface for marking daily attendance and viewing logs with date filtering.
- **Modern Dashboard**: High-level overview of total employees and attendance statistics.
- **Ethara AI Theme**: Premium UI/UX featuring a deep petrol blue palette, crisp typography (Inter), and custom branding elements.
- **Production Ready**: Configured for PostgreSQL and environment-based settings.

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django 4.2+
- **Database**: PostgreSQL (Production), SQLite (local dev support)
- **Frontend**: Vanilla CSS, Semantic HTML5, Font Awesome Icons
- **Deployment**: Gunicorn (WSGI)

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd HRMS
```

### 2. Set up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,localhost

DB_NAME=hrms_db
DB_USER=hrms_user
DB_PASSWORD=strongpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Database Setup (PostgreSQL)
Ensure PostgreSQL is running and execute:
```bash
sudo -u postgres psql -c "CREATE DATABASE hrms_db;"
sudo -u postgres psql -c "CREATE USER hrms_user WITH PASSWORD 'strongpassword';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hrms_db TO hrms_user;"
sudo -u postgres psql -d hrms_db -c "ALTER SCHEMA public OWNER TO hrms_user;"
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Start the Application
```bash
# For development
python manage.py runserver

# For production
gunicorn hrms_project.wsgi:application --bind 0.0.0.0:8000
```
Visit `http://127.0.0.1:8000` to access the portal.

## 🎨 Branding Note
This application uses the **Ethara.AI** visual identity, optimized for recruiters and professional HR environments.

---
© 2026 Ethara AI. All rights reserved.
