class bus:
    def __init__(self):
        self.seats=[1,2,3,4,5]
        self.book_seat=[]

    def seat_booking(self):
        n= int(input("Enter seat no to book"))
        if n not in self.seats:
            print("{n} not a valid seat number")
        elif n in self.book_seat:
            print(f"{n}seat is already booked")
        else :
            self.book_seat.append(n)
            print(f"your seat number {n} is booked successfully...")            
    
    def seat_check(self):
        available = [seat for seat in self.seats if seat not in self.book_seat]
        print("available seats :",available)

    def cancel_seat(self):
        cancel=int(input("enter seat number to cancel"))
        try :
            self.book_seat.remove(cancel)   
            print(f"seat number {cancel} cancel successfully...")     
        except ValueError:
            print("enter valid seat nummber")
b= bus()
while True:
    ch= int(input("what you want to do 1.book seat 2.check available seat 3. cancel seat 4.Exit"))
    match ch:
        case 1: 
          b.seat_booking()
        case 2:
            b.seat_check()
        case 3:
            b.cancel_seat()
        case 4:
            print("exiting..")
            break
