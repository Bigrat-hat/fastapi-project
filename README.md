# 🛒 FastAPI Products Manager

A full-stack product management app built with **FastAPI**, **PostgreSQL on AWS RDS**, and a modern glassmorphism frontend.

![Tech Stack](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Features

- ✅ **REST API** — Create, Read, Delete products
- ✅ **PostgreSQL** on AWS RDS (persistent cloud database)
- ✅ **Modern UI** — Dark glassmorphism frontend (HTML/CSS/JS)
- ✅ **Live stats** — Total products, average price, API status
- ✅ **Search & filter** products in real-time
- ✅ **Deployed on AWS** — EC2 (backend) + S3 (frontend)

---

## 🏗️ Tech Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Backend    | FastAPI + Uvicorn              |
| Database   | PostgreSQL (AWS RDS)           |
| ORM        | SQLAlchemy                     |
| Frontend   | HTML, CSS, Vanilla JS          |
| Hosting    | AWS EC2 (API) + S3 (Frontend)  |

---

## ⚙️ Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-project.git
cd fastapi-project
```

### 2. Create virtual environment & install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your database credentials
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

| Method | Endpoint           | Description          |
|--------|--------------------|----------------------|
| GET    | `/`                | Health check         |
| GET    | `/products`        | List all products    |
| POST   | `/products`        | Add a new product    |
| DELETE | `/products/{id}`   | Delete a product     |

---

## ☁️ AWS Architecture

```
Browser → S3 (index.html) → EC2 (FastAPI :8000) → RDS (PostgreSQL)
```

- **RDS Security Group**: Only allows inbound port 5432 from EC2 security group
- **EC2 Security Group**: Allows port 8000 (API) and port 22 (SSH)

---

## 📁 Project Structure

```
fastapi-project/
├── main.py           # FastAPI app + CORS setup
├── database.py       # SQLAlchemy engine & session
├── models.py         # Product database model
├── schemas.py        # Pydantic schemas
├── routers/
│   └── products.py   # Product CRUD routes
├── index.html        # Frontend UI
├── requirements.txt  # Python dependencies
└── .env.example      # Environment variable template
```

---

## 🔐 Security Notes

- `.env` is in `.gitignore` — never commit real credentials
- RDS is locked down to EC2 security group only (no public access)

---

*Built as part of a full-stack AWS deployment learning project.*
