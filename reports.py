def count_tickets_by_status(tickets):
    counts = {
        "pending": 0,
        "in_progress": 0,
        "resolved": 0
    }

    for ticket in tickets:
        status = ticket["status"]

        if status in counts:
            counts[status] += 1

    return counts


def generate_report(tickets):
    report = {
        "total_tickets": len(tickets),
        "tickets_by_status": count_tickets_by_status(tickets)
    }

    return report