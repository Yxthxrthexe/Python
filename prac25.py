class Train:
    def __init__(self):
        pass
    def getStatus(self, name ,fare,seats):
        print("The name of the Train is ",name)
        print("The Seat available in the train is ",seats)
        print("The price of the ticket is Rs.",fare)
    def bookTickets(self, seatno,seats):
        if(seats>0):
            print("Your ticket is booked and Your seatno is ",seatno)
            seats = seats-1
        else:
               print("no tickets available!!")
intercity = Train()
intercity.getStatus("Intercity Express SuperFast", 95,300)
intercity.bookTickets(34,300)


