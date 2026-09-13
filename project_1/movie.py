class Movie:
    def __init__(self):
        self.seats = [
            ["A1","A2","A3","A4","A5","A6","A7","A8","A9"], 
            ["B1","B2","B3","B4","B5","B6","B7","B8","B9"],  
            ["C1","C2","C3","C4","C5","C6","C7","C8","C9"]  
        ]
        self.booked = []

    def select_show(self):
        n = int(input("Enter the show to book (1, 2, or 3): "))
        if n == 1:
            print("You selected 1st show")
        elif n == 2:
            print("You selected 2nd show")
        elif n == 3:
            print("You selected 3rd show")

    def available_seats(self):
        print("\nAvailable seats:")
        for row in self.seats:
            available = [seat for seat in row if seat not in self.booked]
            print(available)

    def get_ticket_price(self, seatno):
        if seatno.startswith("A"):
            return 320 
        elif seatno.startswith("B"):
            return 280 
        elif seatno.startswith("C"):
            return 240
        else:
            return 0

    def tax_calculation(self, base_price):
        service_tax = base_price * 0.14
        swachh_bharat = base_price * 0.005
        krishi_kalyan = base_price * 0.005
        total_price = base_price + service_tax + swachh_bharat + krishi_kalyan
        return total_price

    def check_seat(self):
        self.available_seats() 
        seatno = input("\nEnter seat to book (Platinum A1-A9, Gold B1-B9, Silver C1-C9): ").upper()
        if seatno in self.booked:
            print(f"Seat {seatno} is already booked.")
        else:
            if any(seatno in row for row in self.seats):
                self.booked.append(seatno)
                price = self.get_ticket_price(seatno)
                total_price = self.tax_calculation(price)
                print(f"Your show is booked successfully!")
                print(f"subotal: ₹{price}")
                print(f"Total (incl. taxes): ₹{total_price:.2f}")
            else:
                print("Invalid seat number. Please try again.")


movie = Movie()
movie.select_show()
movie.check_seat()
movie.check_seat()  
