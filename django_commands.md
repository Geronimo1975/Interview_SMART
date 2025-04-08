# Django Commands Reference

This document contains common Django commands for setting up projects, creating apps, managing migrations, and other useful operations for the Interview_SMART application.

## Environment Setup

### Create a virtual environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Install Django and dependencies
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install Django alone
pip install django
```

## Project Management

### Create a new Django project
```bash
django-admin startproject interview_smart .
```

### Create a new Django app
```bash
python manage.py startapp accounts
python manage.py startapp interviews
python manage.py startapp core
```

### Run development server
```bash
python manage.py runserver
# Specify port (optional)
python manage.py runserver 8080
```

## Database Management

### Create migrations
```bash
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for a specific app
python manage.py makemigrations interviews
```

### Apply migrations
```bash
# Apply all migrations
python manage.py migrate

# Apply migrations for a specific app
python manage.py migrate interviews
```

### Show migration status
```bash
python manage.py showmigrations
```

### Run SQL for migration
```bash
# Show SQL for a migration without applying it
python manage.py sqlmigrate interviews 0001
```

## User Management

### Create superuser
```bash
python manage.py createsuperuser
```

### Change user password
```bash
python manage.py changepassword username
```

## Shell and Database Access

### Django shell
```bash
# Regular shell
python manage.py shell

# Shell plus (if django-extensions installed)
python manage.py shell_plus
```

### Database shell
```bash
python manage.py dbshell
```

## Testing

### Run tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test interviews

# Run specific test class
python manage.py test interviews.tests.TestInterviewModel

# Run with coverage (if installed)
coverage run --source='.' manage.py test
coverage report
```

## Static Files and Assets

### Collect static files
```bash
python manage.py collectstatic
```

### Find static files
```bash
python manage.py findstatic css/style.css
```

## Internationalization

### Create or update message files
```bash
python manage.py makemessages -l de  # Create German translations
```

### Compile message files
```bash
python manage.py compilemessages
```

## Maintenance and Cleanup

### Clear sessions
```bash
python manage.py clearsessions
```

### Check for any issues
```bash
python manage.py check
```

## Deployment Commands

### Check deployment readiness
```bash
python manage.py check --deploy
```

### Run WSGI server with Gunicorn
```bash
gunicorn interview_smart.wsgi:application
```

## Custom Commands for Interview_SMART

You may create custom management commands for application-specific tasks:

```bash
# Create initial data for the application
python manage.py populate_initial_data

# Import standard questions
python manage.py import_questions fixtures/standard_questions.json

# Generate test data
python manage.py generate_test_data
```

## Creating Custom Commands

To create a custom command, add a file to `management/commands/` directory in your app:

```python
# interviews/management/commands/populate_initial_data.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Your code here
        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
```

## Common Django Settings

Important settings to configure in `settings.py`:

```python
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'interview_smart',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```