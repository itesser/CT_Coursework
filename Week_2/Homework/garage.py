from random import randint

class Garage:
    '''
    Simulating a parking garage
    Each object in this class is a car that tries to pull into the garage.


    Class Attributes:
    --------
    Spaces: list of all valid parking spots in the garage
    Ticket: tickets are defined by color and correlate to the number of spaces in the garage 
        so that the attendant can track how many spaces are left.
    
    Object Attributes:
    --------
    plate_num: string input for object initialization and ticket idetification
    can_enter: Bool determined by the number of spaces. If no spaces are available, 
        this is set as False and the car will not be able to access Garage methods
    car_ticket: dictionary contaning information about the car's status in the garage
    -- id : pulled from plate_num gathered when car approached the garage
    -- space: randomly assigned space from available spaces
    -- ticket: pulled from the top (end) of the attendant's stack. 
        The closer the color is to red, the fewer tickets remain. 
            ((this measure of remaining tickets is less useful after the garage reaches capacity))
    -- price: demand-based price set when ticket is issued.
    -- paid: payment status


    Class Methods:
    ---------
    __init__: makes note of car's license plate if space is available. Denies entry if garage is full
    __repr__: Displays car's ticket color and parking location if car is in garage. Denies knowledge of car otherwise.
    take_ticket: Creates Current Ticket dict. 
        Checks to see if:
        - car has already been denied entry due to capacity
        - car already has a ticket
        - (*edge case*) car has exited(destryoed ticket) and is trying to re-enter, but the garage is full
    pay_for_parking: Checks conditions of the object then asks for payment. 
        Any form/amount of payment is accepted. 'Paid' flag set to True.
        Rejected conditions:
        - Car has been allowed to enter
        - Car has recieved ticket/spot assignement
        - Car has already paid
    leave_garage: returns spot assignment and ticket color to their respective inventories. destroys ticket dict.

    Sample commands can be found in comments at the end of the file.

    '''
    
    spaces = ['Floor 1, front', 'Floor 1, middle', 'Floor 1, back', 'Floor 2, front', 'Floor 2, middle', 'Floor 2, back']
    tickets = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'White']
    
    def __init__(self, license_plate):
        if len(self.tickets) == 0:
            self.can_enter = False
            print("Lot is full, please go elsewhere")
        else:
            self.plate_num = license_plate
            self.can_enter = True
            print("spaces are available. Take a ticket to park")
            
    def __repr__(self):
        if hasattr(self, 'car_ticket'):
            return f"Car with plate {self.car_ticket['id']} has the {self.car_ticket['ticket']} ticket and is parked at {self.car_ticket['space']}"
        else:
            return "That car may have visited our garage, but it is not parked here"

    def take_ticket(self):
        if self.can_enter == False or len(self.tickets)==0:
            return "Garage is full, please go elsewhere"
        elif hasattr(self, 'car_ticket'):
            return "You already have a ticket"
        else:
            self.car_ticket = {
                'id': self.plate_num,
                'space': self.spaces.pop(randint(0,len(self.spaces))-1),
                'ticket': self.tickets.pop(),
                'price': 10-len(self.spaces),
                'paid': False
                }

    def pay_for_parking(self):
        if self.can_enter == False:
            return "You are not parked here. Look elsewhere for your car"
        elif not hasattr(self, 'car_ticket'):
            return "You don't have a ticket, please take one before paying"
        elif self.car_ticket['paid'] == True:
            return "You have already paid, please exit the garage"
        else:
            while True:
                payment = input(f"Enter ${self.car_ticket['price']} to pay for your parking: ")
                if payment:
                    print("Payment received, you have 15 minutes to exit")
                    self.car_ticket['paid'] = True
                    break

    def leave_garage(self):
        if self.can_enter == False or not hasattr(self, 'car_ticket'):
            return "How did you get in there? You need a ticket to be in there!"
        elif self.car_ticket['paid'] == False:
            return "Please pay before exiting"
        else:
            self.spaces.append(self.car_ticket['space'])
            self.tickets.append(self.car_ticket['ticket'])
            del self.car_ticket
            return f"Bye  {self.plate_num}! Have a good one!"


# car1 = Garage('2343')
# car1.pay_for_parking()
# print(car1)
# car1.take_ticket()
# print(car1)
# car1.pay_for_parking()
# print(car1)
# car1.leave_garage()
# 
# car2 = Garage('666')
# car2.take_ticket()
# car3 = Garage('34546')
# car3.leave_garage()
# car3.take_ticket()
# car4 = Garage('56452')
# car4.pay_for_parking()
# car4.take_ticket()
# car5 = Garage('111')
# car5.take_ticket()
# 
# all_cars = [car1, car2, car3, car4, car5]
# 
# for car in all_cars:
#     print(car)
# 
# car1= Garage('245354')
# 
# car1.take_ticket()
# car1.pay_for_parking()
# car1.pay_for_parking()
# car1.leave_garage()
# car1.leave_garage()