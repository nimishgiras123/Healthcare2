## 📄 Original Assignment: Django Healthcare Backend

### Objective
The goal of this assignment is to create a backend system for a healthcare application using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
The system should allow users to register, log in, and manage patient and doctor records securely.

### Requirements
- Use Django and Django REST Framework (DRF) for the backend.  
- Use PostgreSQL as the database.  
- Implement **JWT authentication** for user security using `djangorestframework-simplejwt`.  
- Create RESTful API endpoints for managing patients and doctors.  
- Use Django ORM for database modeling.  
- Implement error handling and validation.  
- Use **environment variables** for sensitive configurations.  

### APIs to be Implemented

#### 1. Authentication APIs
- `POST /api/auth/register/` - Register a new user with name, email, and password.  
- `POST /api/auth/login/` - Log in a user and return a JWT token.  

#### 2. Patient Management APIs
- `POST /api/patients/` - Add a new patient (Authenticated users only).  
- `GET /api/patients/` - Retrieve all patients created by the authenticated user.  
- `GET /api/patients/<id>/` - Get details of a specific patient.  
- `PUT /api/patients/<id>/` - Update patient details.  
- `DELETE /api/patients/<id>/` - Delete a patient record.  

#### 3. Doctor Management APIs
- `POST /api/doctors/` - Add a new doctor (Authenticated users only).  
- `GET /api/doctors/` - Retrieve all doctors.  
- `GET /api/doctors/<id>/` - Get details of a specific doctor.  
- `PUT /api/doctors/<id>/` - Update doctor details.  
- `DELETE /api/doctors/<id>/` - Delete a doctor record.  

#### 4. Patient-Doctor Mapping APIs
- `POST /api/mappings/` - Assign a doctor to a patient.  
- `GET /api/mappings/` - Retrieve all patient-doctor mappings.  
- `GET /api/mappings/<patient_id>/` - Get all doctors assigned to a specific patient.  
- `DELETE /api/mappings/<id>/` - Remove a doctor from a patient.  

### Instructions
- Set up a Django project with Django REST Framework and PostgreSQL.  
- Use Django ORM for database interaction.  
- Implement authentication using JWT with `djangorestframework-simplejwt`.  
- Secure patient and doctor-related endpoints with authentication permissions.  
- Follow best practices for structuring the project.  
- Test all API endpoints using **Postman** or any API client.  

### Expected Outcome
- Users should be able to register and log in.  
- Authenticated users should be able to add and manage patient and doctor records.  
- Patients should be assignable to doctors.  
- Data should be stored securely in PostgreSQL.  

**Good luck! 🚀** 

# 🏥 SOLUTION:  Healthcare Backend

A secure backend system for a healthcare application, built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
This backend provides APIs for **user authentication**, **patient and doctor management**, and **patient-doctor mappings**.

---

## ✨ Features

- 🔑 **Authentication** with JWT (Register, Login)
- 🧑‍🤝‍🧑 **Patient & Doctor Management** (CRUD APIs)
- 🔗 **Patient-Doctor Mappings**
- 📦 **PostgreSQL Database Integration**
- 🔒 **Secure Endpoints** with token-based authentication

---

## 📌 API Endpoints & Examples

### 1. Authentication

#### 🔹 Register
**POST** `/api/auth/register/`  
Request:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
````

Response:

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
```

#### 🔹 Login

**POST** `/api/auth/login/`
Request:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

---

### 2. Patient Management

#### 🔹 Add Patient

**POST** `/api/patients/` *(auth required)*
Request:

```json
{
  "name": "Alice Smith",
  "age": 30,
  "gender": "Female",
  "phone": "9876543210",
  "address":"street 123",
  "email":"aliceS@gmail.com"
}
```

Response:

```json
{
    "id": 1,
    "name": "Alice Smith",
    "age": 30,
    "gender": "Female",
    "phone": "9876543210",
    "address": "street 123",
    "email": "aliceS@gmail.com",
    "created_at": "2025-09-20T21:19:32.767840Z",
    "user": 1
}
```

#### 🔹 List Patients

**GET** `/api/patients/`
Response:

```json
[
    {
        "id": 1,
        "name": "Alice Smith",
        "age": 30,
        "gender": "Female",
        "phone": "9876543210",
        "address": "street 123",
        "email": "aliceS@gmail.com",
        "created_at": "2025-09-20T21:19:32.767840Z",
        "user": 1
    }
]
```

---

### 3. Doctor Management

#### 🔹 Add Doctor

**POST** `/api/doctors/` *(auth required)*
Request:

```json
{
  "name": "Dr. Robert Brown",
  "specialization": "Cardiologist",
  "phone": "9123456780",
  "age":21,
  "gender":"male",
  "email":"Robert.brown@gmail.com",
  "address": "245 main strt"
}
```

Response:

```json
{
    "id": 1,
    "name": "Dr. Robert Brown",
    "age": 21,
    "gender": "male",
    "specialization": "Cardiologist",
    "email": "Robert.brown@gmail.com",
    "phone": "9123456780",
    "address": "245 main strt",
    "created_at": "2025-09-20T21:23:24.527748Z",
    "user": 1
}
```

#### 🔹 List Doctors

**GET** `/api/doctors/`
Response:

```json
[
    {
        "id": 1,
        "name": "Dr. Robert Brown",
        "age": 21,
        "gender": "male",
        "specialization": "Cardiologist",
        "email": "Robert.brown@gmail.com",
        "phone": "9123456780",
        "address": "245 main strt",
        "created_at": "2025-09-20T21:23:24.527748Z",
        "user": 1
    }
]
```

---

### 4. Patient-Doctor Mappings

#### 🔹 Assign Doctor to Patient

**POST** `/api/mappings/` *(auth required)*
Request:

```json
{
  "patient": 1,
  "doctor": 1
}
```

Response:

```json
{
    "id": 1,
    "assigned_at": "2025-09-20T21:26:42.200203Z",
    "patient": 1,
    "doctor": 1,
    "user": 1
}
```

#### 🔹 List Mappings

**GET** `/api/mappings/`
Response:

```json
[
    {
        "id": 1,
        "assigned_at": "2025-09-20T21:26:42.200203Z",
        "patient": 1,
        "doctor": 1,
        "user": 1
    }
]
```

---

## ⚙️ Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/nimishgiras123/Healthcare2.git
cd Healthcare2
```

### 2. Setup Environment Variables

Create a `.env` file in the project root and configure:

```env
DB_LIVE=True/False
DB_NAME=<your_database_name>
DB_USER=<your_username>
DB_PASSWORD=<your_password>
DB_HOST=<your_host>
DB_PORT=<your_port>
```

* `DB_LIVE` is used as a **flag variable** to determine which database backend to use:

  * If `DB_LIVE = False`, the project defaults to **SQLite3** (`db.sqlite3`) for local development.
  * If `DB_LIVE = True`, the project connects to a **PostgreSQL server** (either cloud-hosted or locally managed via **pgAdmin**).


Example (for local PostgreSQL setup):

```env
DB_LIVE=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Development Server

```bash
python manage.py runserver
```

---

## 🧪 API Testing & Authentication

- All REST APIs were validated using **Postman**.  
- Authentication is implemented using **JWT (JSON Web Tokens)**.  
- A valid access token must be obtained from the authentication endpoint (`/api/auth/login/`).  

### Postman Setup
1. Navigate to the **Authorization** tab.  
2. Select **Bearer Token**.  
3. Paste the issued **access token** into the input field.  

### Authentication Rules
- Only requests containing a valid header will be processed:
Authorization: Bearer <access_token>
- Authenticated endpoints return standard HTTP status codes:
- **200 OK** → Successful `GET` / `PUT` / `DELETE` operations  
- **201 Created** → Successful `POST` operations  
- Requests without a valid token will be rejected with:
- **401 Unauthorized**  

---

---

## 🚀 Deployment

- **Live URL:** [https://healthcare2-9jns.onrender.com/](https://healthcare2-9jns.onrender.com/)  
- **Database:** Neon PostgreSQL (configured via environment variables)  
- The cloud database currently has **no sample data**, primarily set up for testing user interactions.  

### Testing Notes
- The original assignment document outlines **all required APIs** (Authentication, Patient, Doctor, and Patient-Doctor Mappings).  
- In this README, **some API examples are not explicitly shown**, but they follow the same request/response JSON format as demonstrated.  
- Sample JSON payloads for **User**, **Patient**, and **Doctor** are included in this repository for testing purposes.  
- You can test all endpoints on the deployed instance using **Postman** by following the authentication steps (Bearer Token) as described above.  
  

