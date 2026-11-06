from users import (
    students,
    staff_members,
    register_student,
    register_staff,
    find_student
)

from tickets import (
    tickets,
    create_ticket,
    update_ticket_status
)

from reports import generate_report


def main():
    while True:
        print("\n===== CAMPUSHELP TICKET SYSTEM =====")
        print("1. Register Student")
        print("2. Register Support Staff")
        print("3. Create Ticket")
        print("4. View Tickets")
        print("5. Update Ticket Status")
        print("6. Generate Report")
        print("q. Quit")

        choice = input("\nChoose an option: ").strip().lower()

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")

            if register_student(name, email):
                print("Student registered successfully!")
                print("Student ID:", students[-1]["student_id"])
            else:
                print("Student registration failed.")

        elif choice == "2":
            name = input("Enter staff name: ")
            email = input("Enter staff email: ")

            if register_staff(name, email):
                print("Staff registered successfully!")
                print("Staff ID:", staff_members[-1]["staff_id"])
            else:
                print("Staff registration failed.")

        elif choice == "3":
            try:
                student_id = int(input("Enter your student ID: "))
            except ValueError:
                print("Student ID must be a number.")
                continue

            student = find_student(student_id)

            if student is None:
                print("Student not found. Please register first.")
                continue

            category = input("Enter ticket category: ")
            description = input("Describe your problem: ")
            priority = input("Enter priority (low/medium/high): ").strip().lower()

            ticket = create_ticket(
                tickets,
                student_id,
                category,
                description,
                priority
            )

            if ticket is None:
                print("Ticket creation failed. Check your details.")
            else:
                print("Ticket created successfully!")
                print(ticket)

        elif choice == "4":
            if not tickets:
                print("No tickets recorded yet.")
            else:
                for ticket in tickets:
                    print(ticket)

        elif choice == "5":
            try:
                ticket_id = int(input("Enter ticket ID: "))
            except ValueError:
                print("Ticket ID must be a number.")
                continue

            new_status = input(
                "Enter new status (pending/in_progress/resolved): "
            ).strip().lower()

            updated_ticket = update_ticket_status(
                tickets, ticket_id, new_status
            )

            if updated_ticket is None:
                print("Ticket update failed. Check the ID and status.")
            else:
                print("Ticket updated successfully!")
                print(updated_ticket)

        elif choice == "6":
            report = generate_report(tickets)
            print("\n===== TICKET REPORT =====")
            print(report)

        elif choice == "q":
            print("Thank you for using CampusHelp!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()