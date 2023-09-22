class Garage:
    spaces = ['front', 'middle', 'back']
    tickets = ['red', 'blue', 'green']
    ticket_price = 4
    
    def __init__(self, license_plate):
        if len(self.spaces) == 0:
            print("Lot is full, please go elsewhere")
            self.can_enter = False
        else:
            self.plate_no = license_plate
            self.can_enter = True

    def __repr__(self):
        try:
            return f"Car with plate {self.current_ticket['id']} has ticket {self.current_ticket['ticket']} and is parked at {self.current_ticket['space']}"
        except:
            return "That car may have visited our garage, but it is not parked here"

    def take_ticket(self):
        if self.can_enter == False or len(self.spaces)==0:
            print("Garage is full, please go elsewhere")
        else:
            self.current_ticket = {
                'id': self.plate_no,
                'space': self.spaces.pop(),
                'ticket': self.tickets.pop(),
                'paid': False
                }

    def pay_for_parking(self):
        if self.can_enter == False:
            print("You are not parked here. Look elsewhere for your car")
        else:
            try:
                self.current_ticket
            except:
                return "You don't have a ticket, please take one before paying"
            while True:
                payment = input(f"Enter ${self.ticket_price} to pay for your parking: ")
                if payment:
                    print("Payment received, you have 15 minutes to exit")
                    self.current_ticket['paid'] = True
                    self.spaces.append(self.current_ticket['space'])
                    self.tickets.append(self.current_ticket['ticket'])
                    del self.current_ticket
                    break


# car1 = Garage('2343')
# print(car1)
# car1.take_ticket()
# print(car1)
# car1.pay_for_parking()
# print(car1)

# car2 = Garage('666')
# car2.take_ticket()
# car3 = Garage('34546')
# car3.take_ticket()
# car4 = Garage('56452')
# car4.take_ticket()
# car5 = Garage('111')
# car5.take_ticket()

# all_cars = [car1, car2, car3, car4, car5]

# for car in all_cars:
#     print(car)

car1= Garage('245354')

car1.take_ticket()
car1.pay_for_parking()
car1.pay_for_parking()