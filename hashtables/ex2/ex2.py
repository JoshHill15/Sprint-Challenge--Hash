#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    arr = []
    hm = {}
    for ticket in tickets:
        if ticket not in hm:
            hm[ticket.source] = ticket.destination
    # while len(arr) < 1:
    key = "NONE"
    while key is not None:
        if key is "NONE":
            arr.append(hm[key])
            key = hm[key]

        if len(arr) >= 1:
            arr.append(hm[key])
            key = hm[key]

        if len(arr) == length:
            key = None

    return arr


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]
print(reconstruct_trip(tickets, len(tickets)))
