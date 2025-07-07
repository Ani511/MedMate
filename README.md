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
│ ├── main.py # Entry point
│ ├── scheduler.py # Background jobs (ping/email)
│ ├── routers/ # API routes (meds, reminders)
│ ├── models.py, crud.py # DB logic
│ └── ... # Other configs
│
└── medmate-frontend/ # React frontend
├── src/components/ # ReminderForm, MedicineSearch, etc.
├── public/ # Logos, manifest
└── ... # Tailwind & App setup
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


