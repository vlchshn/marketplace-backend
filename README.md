# HexaStore API

HexaStore is a high-performance REST API for a marketplace platform, built with Python and FastAPI. It provides a
complete backend solution for managing users, products, and orders in a secure and scalable environment.

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
├── alembic/                   # Database migrations configuration
│   ├── versions/              # Migration scripts (history of DB changes)
│   │   ├── ..._initial_migration.py
│   │   ├── ..._create_products_table.py
│   │   └── ..._create_orders_table.py
│   ├── env.py                 # Alembic environment setup (connects to app models)
│   └── script.py.mako         # Template for generating new migrations
│
├── app/                       # Main application source code
│   ├── api/
│   │   ├── routers/           # API Endpoints (Controllers)
│   │   │   ├── auth.py        # Authentication routes (login, register)
│   │   │   ├── products.py    # Product management routes
│   │   │   └── orders.py      # Order processing routes
│   │   └── deps.py            # Dependency Injection (e.g., get_current_user, get_db)
│   │
│   ├── core/                  # Global configs and security
│   │   ├── config.py          # Environment settings (Pydantic Settings)
│   │   └── security.py        # Password hashing and JWT token generation
│   │
│   ├── db/                    # Database connection logic
│   │   └── session.py         # Async engine and session maker setup
│   │
│   ├── models/                # SQLAlchemy ORM Models (Database Tables)
│   │   ├── __init__.py        # Exports models for Alembic
│   │   ├── base.py            # Declarative base class
│   │   ├── user.py            # User model
│   │   ├── product.py         # Product model
│   │   └── order.py           # Order model
│   │
│   ├── schemas/               # Pydantic Schemas (Data Validation & Serialization)
│   │   ├── user.py            # User registration/response schemas
│   │   ├── product.py         # Product creation/view schemas
│   │   ├── order.py           # Order creation schemas
│   │   └── token.py           # JWT Token schema
│   │
│   ├── services/              # Business logic layer (scalable structure)
│   │
│   └── main.py                # Application entry point (FastAPI initialization)
│
├── .env                       # Environment variables (secrets, DB credentials)
├── .gitignore                 # Files to exclude from Git
├── alembic.ini                # Main configuration file for Alembic
├── docker-compose.yml         # Docker services orchestration (App + DB)
├── Dockerfile                 # Instructions to build the API container image
├── poetry.lock                # Locked dependencies versions (for reproducibility)
├── pyproject.toml             # Project metadata and dependencies (Poetry config)
├── requirements.txt           # Legacy dependencies list (for compatibility)
└── README.md                  # Project documentation

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