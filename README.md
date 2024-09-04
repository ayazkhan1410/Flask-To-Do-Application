Here's a README for your Flask To-Do application with registration and login functionality:

---

# Flask To-Do Application

This is a simple Flask-based To-Do application that includes user authentication (registration, login, logout) and CRUD operations for managing tasks. The application uses SQLite as the database and `bcrypt` for password hashing.

## Features

- **User Authentication**: Register, login, and logout functionality with session management.
- **CRUD Operations for To-Dos**: Create, update, delete, and view tasks.
- **Search Functionality**: Filter tasks based on title.
- **Flask Templates**: Dynamic HTML rendering using Flask templates.
- **Password Security**: Secure password storage using `bcrypt` hashing.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- bcrypt

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ayazkhan1410/Flask-To-Do-Application.git
   cd flask-todo-app
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install Flask Flask-SQLAlchemy bcrypt
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

   The application will start on `http://127.0.0.1:5000`.

## Usage

- **Homepage (`/`)**: View all to-dos, create new tasks, and search tasks by title.
- **Update Task (`/update/<sno>`)**: Edit a task based on its serial number (`sno`).
- **Delete Task (`/delete/<sno>`)**: Delete a task based on its serial number (`sno`).
- **About Page (`/about`)**: A static page to provide information about the app.
- **Register (`/register`)**: Create a new user account.
- **Login (`/login`)**: Log in to the application.
- **Logout (`/logout`)**: Log out of the application.

## Application Structure

- **app.py**: Main application file with all route definitions and logic.
- **templates/**: Folder containing HTML templates (`index.html`, `login.html`, `register.html`, `update.html`, `about.html`).

## Database

The application uses SQLite for storing user and task information. The database file `test.db` will be created automatically when you run the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README further as needed!
