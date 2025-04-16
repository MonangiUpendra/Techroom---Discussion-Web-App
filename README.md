# Techroom - Discussion Web App

Techroom is a full-stack discussion-based web application built using Django. It allows users to register, log in, create or join study rooms based on topics, and participate in message-based discussions. The platform is designed to facilitate knowledge sharing and collaboration among learners.

## Features

- User authentication (login/register)
- User profile management
- Topic-based study rooms
- Real-time discussion with messages
- Filtered search by topic or room name
- Avatar support for users
- Mobile-friendly UI

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL (managed with pgAdmin)
- **Version Control:** Git, GitHub

## Project Structure

- `main.html` - Base template
- `login_register.html` - Login/Register switching form
- `room.html` - Room detail and discussion page
- `create-room.html` - Room creation and update form
- `profile.html` - User profile view
- `admin.py` - Admin site configuration
- `models.py` - Custom User model and other data models
- `urls.py` - Route management

## Installation & Setup (Brief)

1. Clone the repository.
2. Set up a virtual environment and install dependencies.
3. Configure PostgreSQL and connect it in `settings.py`.
4. Run migrations and create a superuser.
5. Start the server and access the platform via `localhost`.

## Acknowledgment

This project was developed as part of my learning journey in Python Full Stack Development, showcasing my skills in Django, database handling, and full-stack development.
