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
    allowed_priorities = ["low", "medium", "high"]

    if priority not in allowed_priorities:
        return None
    
    if not description.strip():
        return None

    if not category.strip():
        return None

    if not isinstance(student_id, int) or student_id <= 0:
        return None
    
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




                # Three important functions we have built

                     #   generate_ticket_id() — generates ticket IDs.

                     #   create_ticket() — creates and stores tickets.

                     #   find_ticket() — searches for tickets using their IDs.
