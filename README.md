# Flask Authentication App

A simple web application demonstrating user authentication with Flask, built as a learning project to understand web security fundamentals.

## Learning Intent

This project was created to explore and understand:
- **Web authentication fundamentals** - How login/logout systems work
- **Password security** - Proper hashing techniques and why they matter
- **Session management** - How web applications maintain user state
- **Database integration** - Working with SQLAlchemy ORM
- **Modern web styling** - Creating responsive, accessible interfaces
- **Security best practices** - Input validation, error handling, and secure coding patterns

The goal is to build a solid foundation in web security concepts before moving on to more advanced topics like two-factor authentication.

## Features

- **User Registration** - Create new user accounts with validation
- **Secure Login/Logout** - Session-based authentication
- **Password Security** - Bcrypt hashing for secure password storage
- **Input Validation** - Client and server-side form validation
- **Error Handling** - User-friendly error messages
- **Responsive Design** - Modern dark theme with purple/pink colour scheme
- **Mobile-First** - Optimised for all screen sizes

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Bcrypt for password hashing
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns

## Security Considerations

### Why Bcrypt?
This app uses **bcrypt** for password hashing instead of simpler alternatives because:

- **Adaptive hashing** - Can increase computational cost as hardware improves
- **Built-in salt generation** - Prevents rainbow table attacks
- **Timing attack resistance** - Consistent execution time regardless of input
- **Industry standard** - Widely trusted and battle-tested
- **Future-proof** - Designed to remain secure as computing power increases

### Security Features Implemented
- Password hashing with bcrypt (cost factor 12)
- Session-based authentication
- Input validation and sanitisation
- SQL injection prevention via SQLAlchemy ORM
- Error handling without information leakage
- CSRF considerations (ready for token implementation)

## Project Structure

```
flask-auth-app/
├── app.py                 # Main Flask application
├── users.db              # SQLite database (auto-generated)
├── static/
│   └── styles.css        # Custom CSS styling
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Login/registration page
│   └── dashboard.html    # User dashboard
└── README.md             # This file
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-auth-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-bcrypt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

1. **Register a new account** - Click "Register" and provide username/password
2. **Login** - Use your credentials to access the dashboard
3. **Logout** - Click the logout button to end your session

### Validation Rules
- **Username**: Minimum 3 characters, must be unique
- **Password**: Minimum 6 characters

## Future Enhancements

Planning to add these features as learning progresses:

- **Two-Factor Authentication (2FA)** - TOTP with Google Authenticator
- **Password Reset** - Email-based password recovery
- **Rate Limiting** - Prevent brute force attacks
- **CSRF Protection** - Cross-site request forgery prevention
- **Email Verification** - Confirm user email addresses
- **Password Strength Meter** - Real-time password strength feedback
- **Remember Me** - Persistent login sessions
- **Admin Panel** - User management interface

## Learning Resources

Resources used while building this project:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [bcrypt Wikipedia](https://en.wikipedia.org/wiki/Bcrypt)
- [Code With Josh YouTube](https://youtu.be/Fr2MxT9M0V4?si=IaskFUv7mpkaQV0t)

## Security Notes

**This is a learning project and should not be used in production without additional security measures:**

- Change the secret key to a secure, randomly generated value
- Implement HTTPS in production
- Add rate limiting for login attempts
- Implement proper logging and monitoring
- Add CSRF protection
- Use environment variables for configuration
- Implement proper session security headers

## Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to open issues or submit pull requests.

## Licence

This project is open source and available under the [MIT Licence](LICENSE).

---

**Note**: This application is built for educational purposes to understand web authentication concepts. Always follow security best practices when building production applications.