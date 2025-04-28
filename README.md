# Finance Tracker - Django Web Application

![Screenshot 2025-04-28 180729](https://github.com/user-attachments/assets/251dff9e-37b0-469d-ad15-77cd44a9637b)

## Project Overview
The Finance Tracker is a comprehensive personal finance management system built with Django. It helps users:
- Track income and expenses
- Set and monitor financial goals
- Analyze spending patterns
- Export transaction history
- Manage personal budgets effectively

## Key Features

### User Management
- Secure registration and authentication
- Password protection
- Personalized dashboard

### Financial Tracking
- Record income and expenses
- Categorize transactions
- View net savings calculation
- Transaction history with filtering

### Goal Management
- Create financial goals with targets
- Track progress toward goals
- Set deadlines for achievements

### Data Management
- Export transaction data to CSV
- Clean dashboard visualization
- Responsive design for all devices

## Screenshots

### Authentication
![registration page](https://github.com/user-attachments/assets/dcf1544e-ba60-44d4-baf6-1b2029d85fad)
![login page](https://github.com/user-attachments/assets/6cce26bc-5f0e-4a7b-b649-2519f9e64502)

### Dashboard Views
![dashboard](https://github.com/user-attachments/assets/df4f36ce-df5c-42c5-8b7c-553a31eddf5a)
![after filling details dashboard](https://github.com/user-attachments/assets/532acbb1-79c8-4f22-882a-123061f4d85f)

### Transaction Management
![Add transaction](https://github.com/user-attachments/assets/f9dc5631-efcf-4329-bb5e-ae47aead5c78)
![transaction history and export](https://github.com/user-attachments/assets/2df1b123-523f-4777-8dd6-a5b26b065bd4)

### Goal Setting
![Add goal](https://github.com/user-attachments/assets/460ca56d-ec21-4ef7-a0a0-e4eb5a9694c7)

## Installation Guide

### Prerequisites
- Python 3.8+
- Django 4.0+
- PostgreSQL (recommended) or SQLite

### Setup Steps
1. Clone the repository:
   ```bash
   git clone "repository url"
   cd FinanceTracker
   ```

2. Set up virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure database:
   - Rename `.env.example` to `.env`
   - Update database credentials

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create admin user:
   ```bash
   python manage.py createsuperuser
   ```

7. Start development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000`

## Usage Instructions

1. **Registration & Login**
   - Create an account via registration page
   - Log in with your credentials

2. **Dashboard Navigation**
   - View financial summary
   - Access quick action buttons

3. **Transaction Management**
   - Add new income/expense transactions
   - View and filter transaction history
   - Export data to CSV

4. **Goal Setting**
   - Create financial goals
   - Track progress toward targets
   - Update goals as needed

5. **Data Analysis**
   - Monitor spending patterns
   - Review income sources
   - Calculate net savings

## Technology Stack

### Backend
- Django Framework
- Django REST Framework (for potential API expansion)
- PostgreSQL Database
- Django Authentication System

### Frontend
- HTML5, CSS3
- Bootstrap 5
- JavaScript (for interactive elements)
- Chart.js (for future data visualization)

### Development Tools
- Git for version control
- Pip for package management
- VS Code (recommended IDE)

## API Endpoints
(For future API expansion)
```
/api/transactions/       - GET, POST
/api/transactions/<id>/  - GET, PUT, DELETE
/api/goals/              - GET, POST
/api/goals/<id>/         - GET, PUT, DELETE
/api/users/              - GET (admin only)
```

