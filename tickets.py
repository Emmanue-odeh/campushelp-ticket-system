tickets = []

def generate_ticket_id(tickets):
    return len(tickets) + 1

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

print(new_ticket)
print(tickets)