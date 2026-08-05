# Sathik Groups — Commercial Product Catalogue Platform

A commercial product catalogue platform built with **Python Flask**, **Supabase (PostgreSQL)**, **Jinja2 HTML templates**, and **Vanilla CSS**.

---

## 🏛️ Architecture Overview

- **Backend**: Python 3 + Flask (Blueprints architecture).
- **Database**: Supabase PostgreSQL (`supabase` Python SDK).
- **Service Layer**: Dedicated service layer (`services/`) encapsulating database operations.
- **Frontend**: Vanilla HTML5, CSS3, JavaScript, and Flask Jinja2 Template Inheritance.
- **Constraints**: ZERO prices displayed, NO payments, NO checkout, NO orders. Every product features **Request Quote**, **Enquire Now**, **WhatsApp**, and **Call Now** functionality.
- **Future-Ready**: Pre-scaffolded schemas for future expansion.

---

## 🚀 How to Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create or update `.env`:
```env
SUPABASE_URL=https://your-supabase-project.supabase.co
SUPABASE_KEY=your-supabase-anon-or-service-key
```

### 3. Seed Database (Optional)
```bash
python seed.py
```

### 4. Run Flask Application
```bash
python app.py
```

Visit the website at: **[http://localhost:5001](http://localhost:5001)**
Admin Portal: **[http://localhost:5001/login](http://localhost:5001/login)** (Default Credentials: `admin@sathikgroups.com` / `ChangeMe@2024!`)
