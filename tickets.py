tickets = []

def generate_ticket_id(tickets):
    return len(tickets) + 1

def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            return ticket

    return None

def update_ticket_status(tickets, ticket_id, new_status):
    allowed_statuses = ["pending", "in_progress", "resolved"]

    if new_status not in allowed_statuses:
        return None

    ticket = find_ticket(tickets, ticket_id)

    if ticket is None:
        return None
    
    ticket["status"] = new_status

    return ticket

def create_ticket(tickets, student_id, category, description, priority):
    ticket_id = generate_ticket_id(tickets)

    ticket = {
   
        "ticket_id": ticket_id,
        "student_id": student_id,
        "category": category,
        "description": description,
        "priority": priority,
        "status": "pending"
    }
    
    tickets.append(ticket)

    return ticket

              # Three python concepts that have been connected successfully.

                      # Functions — to perform tasks.

                      # Dictionaries — to organise ticket information.

                      # Lists — to store multiple tickets.


new_ticket = create_ticket(
    tickets,
    1,
    "Wi-Fi",
    "Campus Wi-Fi is not working",
    "high"
)
                # Three important functions we have built

                     #   generate_ticket_id() — generates ticket IDs.

                     #   create_ticket() — creates and stores tickets.

                     #   find_ticket() — searches for tickets using their IDs.

second_ticket = create_ticket(
    tickets, 2, "Laptop",
    "My laptop is not working", "medium"
)
found_ticket = find_ticket(tickets, 2)

print(found_ticket)

updated_ticket = update_ticket_status(tickets, 2, "resolved")

print(updated_ticket)