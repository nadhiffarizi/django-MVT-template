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


🚀 How to Use
▶️ Login & Register
Visit /login/ to sign in with your account.

Visit /register/ to create a new account (if included).

Logout using /logout/.

🧑 Admin Panel
Go to /admin/ and log in using the superuser credentials.

From here you can manage users and any models you’ve added.

🛠 Customizing the App
Add a model: define it in myapp/models.py, then run:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create a view: add logic in myapp/views.py and route it in myapp/urls.py.

Create a template: put your .html files in myapp/templates/, and render them from the view using:

python
Copy
Edit
return render(request, 'my_template.html', context)
Style your app: use static files in a static/ directory (add STATICFILES_DIRS to settings if needed).

✨ Features
✅ Django’s built-in authentication system

✅ Admin panel included

✅ Default SQLite DB (zero config)

✅ Uses MVT architecture

✅ Ready for customization

🧪 Testing
Run tests with:

bash
Copy
Edit
python manage.py test
📦 Requirements
Python 3.8+

Django 4.x

SQLite (included by default)
