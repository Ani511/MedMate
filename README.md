# 💊 MedMate

MedMate is a full-stack medicine management and reminder app that helps users:

- Search for nearby pharmacies stocking specific medicines
- Schedule daily medication reminders
- View scheduled doses in a simple, beautiful interface
- (Coming soon) Receive timely email alerts via scheduler

---

## 🖼️ Live Preview

![Webapp Preview](./medmate-frontend/public/preview.png) 

---

## 🚀 Features

- 🔍 **Medicine Search**: Real-time search from local pharmacy database
- ⏰ **Reminders**: Add daily reminders with time and user ID
- 📜 **History**: View past reminders with frontend notifications
- 📬 **Email Integration** *(planned)*: Send reminder copies via email
- 🎨 **Modern UI**: Built using React + TailwindCSS with smooth interactions

---

## 🛠️ Tech Stack

| Frontend        | Backend       | Database    | Other             |
|-----------------|---------------|-------------|-------------------|
| React           | FastAPI       | PostgreSQL  | Axios, Toastify   |
| Tailwind CSS    | REST APIs     | SQLAlchemy  | APScheduler       |

---

## 📁 Folder Structure

```
MedMate/
│
├── Backend/ # FastAPI backend
│ ├── main.py # Main entry point
│ ├── scheduler.py # Background job runner (ping/email)
│ ├── config.py # Future config values (SMTP, env)
│ ├── crud.py # DB utility functions (CRUD ops)
│ ├── database.py # DB connection setup (SQLAlchemy)
│ ├── email_utils.py # Email sending functions (planned for future)
│ ├── models.py # SQLAlchemy models (Medicine, Reminder)
│ ├── schemas.py # Pydantic schemas for validation
│ └── routers/
│ ├── meds.py # /medicines/ API route
│ └── reminders.py # /reminders/ API route
│
├── medmate-frontend/ # React frontend
│ ├── public/ # Static files
│ ├── src/
│ │ ├── App.js # Main app component
│ │ ├── App.css # Styling overrides
│ │ ├── index.js # React entry point
│ │ ├── index.css # Global Tailwind + custom styles
│ │ ├── components/
│ │ │ ├── MedicineSearch.jsx # Medicine search component
│ │ │ ├── ReminderForm.jsx # Reminder input component
│ │ │ └── ReminderList.jsx # Reminder history + toast notifications
│ ├── tailwind.config.js # Tailwind CSS config
│ ├── postcss.config.js # PostCSS processor
│ ├── package.json # Frontend dependencies
├── Readme.md
```
---

## ⚙️ How to Run

### 🧪 Backend (FastAPI + PostgreSQL)

```bash
cd Backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
🔁 Make sure PostgreSQL is running and connected (adjust config if needed)
```
---
### 🖥️ Frontend (React + TailwindCSS)
```bash
cd medmate-frontend
npm install
npm start
App will run on http://localhost:3000 by default.
```
---
### 📌 Upcoming Features
- 📧 Email reminders via SMTP integration
- 🧠 AI-powered medicine suggestions (future)
- 🏥 Location-based pharmacy mapping


