# 🧩 Django MVT Starter App

A simple Django web application using the **MVT (Model-View-Template)** design pattern.  
Includes:

- 🔐 Built-in authentication (login, logout, register)
- 🗃️ Default SQLite database
- 🧱 Clean MVT folder structure
- 🧪 Ready for local development

---

## 📁 Project Structure (MVT)

```bash
project_root/
├── myapp/              # Django app
│   ├── models.py       # Model (data layer)
│   ├── views.py        # View (logic & control)
│   ├── urls.py         # Route definitions
│   ├── templates/      # Template (HTML rendering)
│   └── forms.py        # (Optional) Django forms
├── db.sqlite3          # Default SQLite database
├── manage.py
├── requirements.txt
└── project_name/       # Django project config
    ├── settings.py
    ├── urls.py
    └── wsgi.py
