# Magnus Django Employee CRUD + More Menu

A simple Django implementation for the Magnus/JALA-style developer assignment.
The project focuses on business logic and CRUD operations rather than a complex UI.

## Features

### Employee module
- Login / logout
- Employee Create, Read, Update and Delete (CRUD)
- Search by employee name, mobile number or email
- Pagination
- Employee photo upload
- Date of birth, gender, address, country, city and skills
- Django Admin support

### More Menu
- Multiple Tabs
- Menu / Submenu
- Autocomplete
- Collapsible Content
- Images
- Slider
- Tooltips
- Popups
- Links
- CSS Properties
- iFrames

## Termux setup

```bash
pkg update -y
pkg install python unzip -y
cd ~/storage/downloads
unzip magnus_django_final_termux.zip
cd magnus_django
pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Open:
`http://127.0.0.1:8000/`

Admin:
`http://127.0.0.1:8000/admin/`

## Important

The project includes an initial migration for the Employee model, so a fresh installation creates the `employees_employee` table correctly. `tzdata` is included because Termux/Android may not provide the `Asia/Kolkata` timezone database by default.

Do not commit `db.sqlite3`, real passwords, or uploaded personal files to Git/Bitbucket.
