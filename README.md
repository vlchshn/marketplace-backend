# HexaStore API

HexaStore is a high-performance REST API for a marketplace platform, built with Python and FastAPI. It provides a complete backend solution for managing users, products, and orders in a secure and scalable environment.

## Technical Stack

* Framework: FastAPI (Asynchronous Python framework)
* Database: PostgreSQL (Asynchronous driver asyncpg)
* ORM: SQLAlchemy 2.0 (Modern style with Mapped and mapped_column)
* Migrations: Alembic
* Authentication: JWT (JSON Web Tokens) with OAuth2 password flow
* Validation: Pydantic V2
* Infrastructure: Docker & Docker Compose

## Project Structure

```text
marketplace-backend/
├── alembic/                # Database migrations history and configuration
│   └── versions/           # Migration scripts (Users, Products, Orders)
├── app/
│   ├── api/
│   │   ├── routers/        # API endpoints (auth.py, users.py, products.py, orders.py)
│   │   └── deps.py         # Dependencies (current user, DB session)
│   ├── core/               # Security (JWT, hashing) and global configuration
│   ├── models/             # SQLAlchemy database models (Base, User, Product, Order)
│   ├── schemas/            # Pydantic models for validation and serialization
│   ├── db/
│   │   └── session.py      # Database engine and session management
│   └── main.py             # Application entry point & lifespan management
├── Dockerfile              # Instructions for building the Docker image
├── docker-compose.yml      # Multi-container orchestration (App + PostgreSQL)
├── requirements.txt        # Project dependencies and versions
├── .gitignore              # Files and directories ignored by Git
└── README.md               # Project documentation

```

## Features

* User Management: Secure user registration, authentication, and JWT-based session management.
* Product Catalog: Comprehensive CRUD operations for marketplace products.
* Access Control: Owner-based permissions; only the creator of a product can update or delete it.
* Order System: Automated order creation connecting users with products.
* Database Design: Optimized relational schema with many-to-one relationships.

## Installation and Setup

### Prerequisites

* Docker and Docker Compose installed on your system.

### Running the Application

1. Clone the repository:
```bash
git clone https://github.com/vlchshn/marketplace-backend.git
cd marketplace-backend

```


2. Launch with Docker Compose:
```bash
docker-compose up --build

```


3. Apply Database Migrations:
In a separate terminal window, run the following command to create the database schema:
```bash
docker-compose exec app alembic upgrade head

```



## API Documentation

Once the services are up and running, you can explore and test the API endpoints through the interactive Swagger UI:

URL: [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

---

Developed as a demonstration of modern backend architecture and asynchronous Python development.