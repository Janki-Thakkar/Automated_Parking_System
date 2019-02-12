import random
from Parking_Area import Parking_Area

class Customer:
    Customers = dict()
    def __init__(self, customer_ID):
        '''
        Instantiating a customer object with customer ID
        :param customer_ID: randomly generated customerID
        '''
        self.customer_ID = customer_ID

    def raise_Request(self, customer_ID):
        '''
        Request for parking is raised using the customerID
        :param customer_ID: previously generated customerID
        '''
        print("Is there parking available?")

    def confirm_Request(self, customer_ID):
        '''
        Confirm the request raised once the server asks for response
        :param customer_ID: customerID used to raise the request
        :return: Randomly generated response. Note: The user can select only Y or N as there are buttons.
        '''
        response = random.choice(['Y', 'N', 'n', 'y'])
        return response

    def receive_Confirmation(self, booking_ID):
        '''
        Confirmation with the booking ID is received and is updated to the customer data
        :param booking_ID: The bookingID received once the booking request is successful
        '''
        c1 = Customer
        customer_ID = self.customer_ID
        if customer_ID not in c1.Customers:
            c1.Customers[customer_ID] = dict()
            c1.Customers[customer_ID]['booking_ID'] = booking_ID
        else:
            c1.Customers[customer_ID]['booking_ID'] = booking_ID
        #print(c1.Customers)

    def raise_Entry_Request(self,booking_ID):
        '''
        This function is called once the customer reaches the premises and scans/inputs the bookingID
        :param booking_ID: The booking ID scanned at the entrance
        '''
        print("I would like enter the parking area. My booking ID is:", booking_ID)


    def update_Licence_Plate(self, booking_ID, licence_number):
        '''
        Once the entry is granted the licence plate is generated and updated to the customer records.
        :param booking_ID: Scanned bookingID
        :param licence_number: The car_Licence_Plate_Number scanned at the entrance
        :return:
        '''
        c1 = Customer
        for c in c1.Customers:
            if c1.Customers[c]['booking_ID'] == booking_ID:
                customer_ID = c
        c1.Customers[customer_ID]['car_Number'] = licence_number

    def park_Car(self, booking_ID, available_Spots_ID):
        '''
        This function scans all the available parking spots and chooses one to park the car
        :param booking_ID: The booking ID of the vehicle that has entered the premises
        :param available_Spots_ID: All the spots that are available in the parking lot
        :return: Spot_ID where the car is parked and the licence_plate_Number scanned at the parking spot
        '''
        c1 = Customer
        for c in c1.Customers:
            if c1.Customers[c]['booking_ID'] == booking_ID:
                customer_ID = c
        spot_ID = random.choice(available_Spots_ID)
        return spot_ID, c1.Customers[customer_ID]['car_Number']

    def exit_Premises(self, licence_Number):
        '''
        Function used to exit the premises
        :param licence_Number: The licence number scanned when the car is moved from the parking area and at the exit entrance
        :return: licence number that exited the premises.
        '''
        print('I would like to end my booking')
        return licence_Number

