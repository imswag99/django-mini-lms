# 🎓 e-ducate — Mini LMS

**e-ducate** is a simple, modern DEMO Learning Management System (LMS) built with **Django** and **Tailwind CSS**.  
It allows instructors to create and manage courses, while students can enroll, learn through video lessons, and submit reviews.

---

## 🚀 Features

- 👩‍🏫 Instructor and Student roles  
- 📚 Create, edit, and delete courses  
- 🎥 Add lessons with video links (YouTube or other sources)  
- 🧭 Student enrollment
- ⭐ Reviews and ratings system  
- 📱 Responsive design using Tailwind CSS  
- 🗃️ SQLite database for easy local setup  

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally 👇

### 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/e-ducate.git
cd e-ducate

### 2️⃣ Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Migrations
python manage.py migrate

### 5️⃣ Create a Superuser
python manage.py createsuperuser

### 6️⃣ Start the Development Server
python manage.py runserver

### 7️⃣ Visit the Application
Open your browser and go to:
👉 http://127.0.0.1:8000/
