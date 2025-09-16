# Health ChatBot

## Overview
**Health ChatBot** is a Python-based backend project built using **Django**. The chatbot provides health remedies for various diseases based on user queries. The project currently stores remedy data in a Python file (`remedies.py`) and can respond dynamically. While a SQLite database is included (`db.sqlite3`), it is currently empty as all data is stored in Python files.

---

## Features
- Provides remedies for diseases through a chatbot interface
- Backend powered by Django
- Supports querying remedies dynamically from `remedies.py`
- Easily extendable to use database storage (SQLite) in future
- Virtual environment included for isolated dependency management

---

## Project Structure
backend/
├── backend/ # Django project folder
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── chat/ # Django app folder
├── venv/ # Virtual environment
├── db.sqlite3 # SQLite database (currently empty)
├── manage.py
├── remedies.py # Python file containing disease remedies
├── requirements.txt # Project dependencies
└── README.md

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Kusuma2205/Health-ChatBot.git
cd Health-ChatBot/backend

2.**Activate virtual environment**
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
3.**Install dependencies**


pip install -r requirements.txt


4.**4.Run Django server**

python manage.py runserver

5.**Access the backend**

The server runs locally at: http://127.0.0.1:8000/

You can test your chatbot API endpoints from here.

6.**Usage**

The chatbot fetches remedies from remedies.py based on disease names.

Add new remedies by editing remedies.py in a dictionary format:

remedies = {
    "disease_name": ["remedy1", "remedy2", ...],
}


Responses can later be integrated with a frontend interface.