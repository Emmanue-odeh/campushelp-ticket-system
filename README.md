# CampusHelp Ticket System

## About the Project

CampusHelp is a Python-based command-line ticket management system designed to help students report campus-related problems and allow support staff to manage and track those issues.

The system provides a simple way to register users, create support tickets, update ticket statuses, and generate reports.

## Features

- **Student Registration:** Register students with their names and email addresses.
- **Support Staff Registration:** Register support staff members.
- **Ticket Creation:** Allow registered students to report problems.
- **View Tickets:** Display recorded support tickets.
- **Update Ticket Status:** Change ticket statuses between pending, in progress, and resolved.
- **Generate Reports:** Display the total number of tickets and group them by status.
- **Input Validation:** Validate names, email addresses, ticket descriptions, categories, and priorities.

## Technologies Used

- Python 3
- Git and GitHub

## Project Structure

```text
campushelp-ticket-system/
│
├── main.py
├── users.py
├── tickets.py
├── reports.py
├── validation.py
├── test/
├── README.md
└── .gitignore
```

### File Descriptions

- `main.py` – Runs the application and displays the main menu.
- `users.py` – Handles student and support staff registration.
- `tickets.py` – Handles ticket creation, searching, and status updates.
- `reports.py` – Generates ticket reports.
- `validation.py` – Contains input validation functions.
- `test/` – Contains project testing files.

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Emmanue-odeh/campushelp-ticket-system.git
```

2. Navigate into the project folder:

```bash
cd campushelp-ticket-system
```

3. Run the application:

```bash
python main.py
```

## How to Use

When the application starts, a menu will appear with the following options:

1. Register Student
2. Register Support Staff
3. Create Ticket
4. View Tickets
5. Update Ticket Status
6. Generate Report
7. Quit using `q`

Follow the prompts displayed in the terminal to use the system.

## Current Limitations

- Application data is stored in memory and is not permanently saved.
- Registered users and tickets are lost when the application closes.
- The application currently runs through a command-line interface.

## Future Improvements

- Add database storage for permanent records.
- Develop a graphical user interface.
- Improve user authentication and access control.
- Add more detailed reporting features.

## Contributors

Developed collaboratively as a Python programming project.

