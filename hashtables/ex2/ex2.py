class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    # create a cache and a trip list full of empty slots
    cache = {}
    trip = [None] * length

    # cache all tickets. source as key, value as destination
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # starting flight is flight with key "NONE"
    current = cache['NONE']


    for i in range(length):
        # set trip index at i, and store the cache at current in the trip 
        trip[i] = current
        # move the pointer current in cache to the next one.
        current = cache[current]

    return trip
    

# tests
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
          ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
reconstruct_trip(tickets, 10)