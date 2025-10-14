# Flask Overun - Python Web Application

A Flask web application with SQLAlchemy ORM and PostgreSQL database integration. Demonstrates modern Python web development with database management and user interface.

## Overview

This Flask application showcases:
- Flask web framework
- SQLAlchemy ORM
- PostgreSQL database
- MVC architecture
- Template rendering with Jinja2
- Database migrations
- Configuration management

## Features

- **Web Interface**: Dynamic HTML templates
- **Database Integration**: PostgreSQL with SQLAlchemy
- **User Management**: CRUD operations
- **Modular Design**: Organized project structure
- **Configuration**: Environment-based settings

## Tech Stack

- **Framework**: Flask 3.1.2
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Database**: PostgreSQL (psycopg 3.2.9)
- **Python**: 3.8+

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database
- pip package manager

### Setup

```bash
# Clone repository
git clone <repository-url>
cd project-flask-web-python_flask-overun

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Configure database
# Edit config.py with your PostgreSQL credentials

# Initialize database
python
>>> from app import db
>>> db.create_all()

# Run application
python run.py
```

## Configuration

Edit `config.py`:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
    SECRET_KEY = 'your-secret-key'
```

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── views.py
│   └── templates/
├── models.py
├── routes.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Usage

```bash
# Run development server
python run.py

# Access at http://localhost:5000
```

## Database Models

Define models in `models.py`:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
```

## Routes

Application routes in `routes.py` and `app/views.py`.

## Contributing

See CONTRIBUTING.md for guidelines.

## License

MIT License

---

**Flask Web Application** 🐍
