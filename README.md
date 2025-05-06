# 🛠️ Incident Management System

A simple, open-source **Incident Management System** built with **Flask**, **SQLite**, and **Bootstrap**, 
designed to help teams log, track, and resolve infrastructure or application issues. It features **role-based access**, **email notifications**, and a RESTful API backend.

---

## 📌 Features

- Log incidents with title, description, severity, and status  
- View, assign, and resolve incidents  
- Role-based access control (Admin/User)  
- Email notifications on incident creation and updates  
- RESTful API support  
- Containerized using Docker  

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask  
- **Database**: SQLite  
- **Frontend**: HTML/CSS, Bootstrap  
- **Email**: SMTP (Flask-Mail)  
- **Deployment**: Docker  
- **Version Control**: Git + GitHub  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- pip  
- Docker (optional)  

### 1. Clone the Repository

bash
git clone https://github.com/kavya9864/incident_management.git
cd incident_management

2. Create a Virtual Environment & Install Dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Run the Flask App
   python app.py
visit http://13.48.78.68:8080/
![project 8)](https://github.com/user-attachments/assets/60946be4-1143-414e-bc36-438d476b9fc3)


🧪 API Endpoints
| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | /incidents      | View all incidents  |
| POST   | /incidents      | Create new incident |
| PUT    | /incidents/<id> | Update an incident  |
| DELETE | /incidents/<id> | Delete an incident  |

🧑‍💻 Roles
Admin: Can view, assign, and resolve incidents

User: Can create and view incidents

📧 Email Notifications
Configure your SMTP settings in config.py or a .env file to enable email notifications when:

A new incident is reported

An incident is updated or resolved

📜 License
This project is open-source and available under the MIT License.

## 🙌 Contributors

- [kavya9864](https://github.com/kavya9864/incident_management/tree/master)
