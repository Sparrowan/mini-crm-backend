# Application Setup Guide

This guide will help you set up and run the Django application after cloning the repository from GitHub.

## Prerequisites

Ensure you have the following installed on your system:

- [Python (3.8 or later)](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/) (comes with Python installation)
- [Git](https://git-scm.com/)
- (Optional) [virtualenv](https://virtualenv.pypa.io/en/latest/) for managing virtual environments

---

## Setup Instructions

### 1. Clone the Repository

```bash
git@github.com:Sparrowan/mini-crm-backend.git
cd mini-crm-backend
```
### 2. Create a Virtual Environment

```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```
### 4. Configure Environment Variables

```
Copy the .env-example to a .env file and modify accordilling
```

### 5. Run migrations

```
python manage.py migrate

```
### 6. Running Celery
```
celery -A minicrm worker -l info
```
### 7. Running celery beat

```
celery -A minicrm beat -l inf
```
### 8. Running Flower dashboard

```
celery -A minicrm flower --port=5555
```