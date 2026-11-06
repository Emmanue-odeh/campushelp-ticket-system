from reports import count_tickets_by_status, generate_report


def test_count_tickets_by_status():
    tickets = [
        {"ticket_id": 1, "status": "pending"},
        {"ticket_id": 2, "status": "resolved"},
        {"ticket_id": 3, "status": "pending"},
        {"ticket_id": 4, "status": "in_progress"}
    ]

    result = count_tickets_by_status(tickets)

    assert result["pending"] == 2
    assert result["in_progress"] == 1
    assert result["resolved"] == 1


def test_generate_report():
    tickets = [
        {"ticket_id": 1, "status": "pending"},
        {"ticket_id": 2, "status": "resolved"}
    ]

    result = generate_report(tickets)

    assert result["total_tickets"] == 2
    assert result["tickets_by_status"]["pending"] == 1
    assert result["tickets_by_status"]["resolved"] == 1


def test_empty_ticket_list():
    result = generate_report([])

    assert result["total_tickets"] == 0
    assert result["tickets_by_status"]["pending"] == 0