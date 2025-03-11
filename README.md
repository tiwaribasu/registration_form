project/
├── app.py                  # Main Flask app (minimal)
├── routes/
│   ├── auth.py             # Handles registration, login, and OTP logic
│   ├── admin.py            # Admin page logic
│   └── __init__.py         # Makes `routes` a Python package
├── templates/
│   ├── register.html       # Registration form
│   ├── login.html          # Login form
│   ├── admin.html          # Admin page
│   └── otp.html            # OTP verification form
├── instance/
│   └── site.db             # SQLite database
└── requirements.txt        # Dependencies
