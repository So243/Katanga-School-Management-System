# Katanga-School-Management-System
A Tkinter-based desktop application for managing student information for the Complexe Scolaire Katanga (academic year 2024–2025). This project integrates a MySQL database for persistent storage of student records, enabling registration, listing, and management of student data.
Here's a **professional README** for your GitHub project:

---

# Katanga School Management System

A **Tkinter-based desktop application** for managing student information for the **Complexe Scolaire Katanga** (academic year 2024–2025).
This project integrates a **MySQL database** for persistent storage of student records, enabling registration, listing, and management of student data.

---

## 🚀 Features

* **Login System** (username/password protected).
* **Student Registration** with details like name, gender, date of birth, parents, and contact info.
* **Treeview Table** to display all student records dynamically.
* **Database Integration** with MySQL for secure storage.
* **Interactive GUI** built with `Tkinter` and `ttk`.
* **Image & Logo Display** (via `PIL`).
* **Buttons for:**

  * Registering a student.
  * Clearing form fields.
  * Exiting the application.
* **Scrollable Table** (both horizontal and vertical scroll).

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** (GUI framework)
* **MySQL** (via `mysql-connector-python`)
* **Pillow (PIL)** for image processing
* **Datetime** for date handling

---

## ⚙️ Installation

### **1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/KatangaSchoolManagementSystem.git
cd KatangaSchoolManagementSystem
```

### **2. Install required dependencies**

```bash
pip install mysql-connector-python pillow
```

### **3. Set up the MySQL database**

* Create a database (e.g., `sys`).
* Update the **database connection details** in the code:

  ```python
  self.db_connection = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="YOUR_PASSWORD",
      database="sys"
  )
  ```

### **4. Run the application**

```bash
python main.py
```

---

## 🔑 Default Login

* **Username:** `Katanga` or `Katanga@1`
* **Password:** `123456`

---

## 📸 Screenshots (Optional)

*(You can add screenshots of your app interface here once captured.)*

---

## 📂 Project Structure

```
KatangaSchoolManagementSystem/
│
├── logo.png                  # Logo of the app
├── main.py                   # Main application script
└── README.md                 # Documentation
```

---

## 🤝 Contribution

Want to improve this project? Feel free to fork and create a pull request!

---

## 📜 License

This project is licensed under the **MIT License**.
