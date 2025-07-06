# Videoflix Backend – Django REST API

Videoflix Backend is a RESTful API built with **Django** and **Django REST Framework (DRF)**. It serves as the backend for the Videoflix project, a Netflix-inspired streaming platform.

This repository is intended to work alongside the [Videoflix Frontend](https://github.com/mahapiri/videoflix_frontend), providing all required backend functionality for video streaming, user management, and content organization.
Version: V1.0.0

---

## 🧠 Special Features

- 🎬 **Video Streaming Platform**: Complete backend for a Netflix-like streaming service
- 🔐 **User Authentication & Profiles**: Supports user registration, login, and multiple user profiles
- 📹 **Video Management**: Upload, organize, and stream video content with metadata
- 🎭 **Content Categories**: Genre-based content organization and filtering
- 📱 **Responsive API**: Clean endpoints designed for seamless frontend integration
---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mahapiri/videoflix-backend.git
cd videoflix-backend

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: "env\Scripts\activate"

# Install dependencies
pip install -r requirements.txt
```

### 🔐 Environment Setup



### 🛢️ Database and Static Files Setup

```bash
# Apply migrations
python manage.py migrate

# Create media directories
mkdir -p media/videos media/thumbnails media/profiles

# Collect static files
python manage.py collectstatic

# Run the server
python manage.py runserver
```

### 👑 Admin Access Setup

Create a superuser account to manage content through the Django admin interface:

1. Create a superuser account:
    ```bash
    python manage.py createsuperuser
    ```
2. Complete the prompts for username, email, and password.
3. Visit:
    ```
    http://127.0.0.1:8000/admin/
    ```
4. Log in with your superuser credentials to manage videos, users, and categories.

---

## 🎬 Video Management

The platform supports various video formats and automatic thumbnail generation:

- **Supported formats**: MP4, WebM, AVI
- **Automatic thumbnail extraction**: Thumbnails are generated automatically upon video upload
- **Video metadata**: Title, description, genre, release year, duration
- **Quality options**: Multiple resolution support for adaptive streaming

---

## 🚀 API Documentation

Once the server is running, API documentation is available at:
```
http://localhost:8000/api/schema/redoc/
```

### Main API Endpoints:

- **Authentication**: `/api/auth/`
- **Videos**: `/api/videos/`
---

## 🛠️ Technology Stack

- **Backend Framework**: Django 4.x
- **API Framework**: Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django's built-in authentication + JWT tokens
- **File Storage**: Local storage (development) / AWS S3 (production)
- **Video Processing**: FFmpeg for video processing and thumbnail generation

---

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

---

## 🚀 Deployment

For production deployment, consider:

1. **Environment Variables**: Use production-ready SECRET_KEY and database settings
2. **Database**: Switch to PostgreSQL for better performance
3. **Media Storage**: Use AWS S3 or similar for video file storage
4. **HTTPS**: Enable SSL/TLS for secure streaming
