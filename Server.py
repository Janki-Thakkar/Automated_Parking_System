import random
from Bookings import Booking
from Cars import Car

class Server:
    Bookings = dict()

    def __init__(self, server_ID):
        self.server_ID = server_ID


    def request_Response(self, customer_ID, avail_Spots):
        '''
        Response from the server once the reqiest is generated by the customer
        :param customer_ID: The customerID of the customer raising a booking request
        :param avail_Spots: Number of spots available in the parking lot
        :return: Y if space is available in the parking lot, else N
        '''
        if avail_Spots > 0:
            print("Yes, would you like to book a parking spot? (Y/N)")
            return 'Y'
        else:
            print('Sorry!! The parking is full.')
            return 'N'

    def create_Booking(self, response, avail_Spots):
        '''
        Creates the booking based on the response received from the customer and updates the available spots accordingly
        :param response: Response received from the customer
        :param avail_Spots: Number of spots available in the parking lot
        :return: Booking ID if a booking is made, else 0 and available spots after the booking.
        '''
        if response in ['Y', 'y']:
            book_id = random.randint(10000, 99999)
            b = Booking(book_id)
            booking_Ledger = b.request_accepted(book_id)
            avail_Spots -= 1
            print("Yay! Your spot is booked. Your booking ID is:", book_id)
            #print("Available spots:", avail_Spots)
            return book_id, avail_Spots
        else:
            print("We are sorry to see you go.")
            #print("Available Spots:", avail_Spots)
            return 0, avail_Spots

    def verifyBooking(self,booking_ID):
        '''
        This function is used to verify the booking of the customer when they scan/input the booking_ID at the entrance.
        If the booing is valid, the car licence plate is scanned.
        All the data related to the booking is stored in the dictionary Bookings
        :param booking_ID: The ID scanned/inserted by the customer at the entrance
        :return: car_Licence_Plate_Number scanned at the entrance once the booking is verified
        '''
        b = Booking(booking_ID)
        booking_Ledger = b.get_Bookings()
        if booking_ID in booking_Ledger:
            print('Your booking is valid.')
            c = Car(booking_ID)
            licence_number = c.licence_plate_number()
            b.vehicle_Entered(booking_ID, licence_number)
            print('A car entered with license number:', booking_Ledger[booking_ID]['car_Licence_Plate_Number'])
            return licence_number

    def update_Records(self, booking_ID, spot_ID):
        '''
        Updates the spotID where the car is parked if a park request is raised by the bookingID
        :param booking_ID: The bookingID of the car that raises the Park request
        :param spot_ID: The spotID where the car is parked.
        '''
        b = Booking(booking_ID)
        booking_Ledger = b.get_Bookings()
        b.vehicle_Parked(booking_ID, spot_ID)
        s1 = Server
        print('Vehicle with license plate number {} parked at {}'
              .format(booking_Ledger[booking_ID]['car_Licence_Plate_Number'], spot_ID))

    def endBooking(self,booking_ID):
        '''
        This function marks the exit of a vehicle from the premises and updates the Booking ledger dictionary with the
        exit time and booking status.
        :param booking_ID: BookingID of the car that left the premises
        :return: SpotID where the car was parked if it was parked else 0
        '''
        b = Booking(booking_ID)
        booking_Ledger = b.get_Bookings()
        b.vehicle_Left(booking_ID)
        print('A vehicle exited. Booking with Booking ID {} is completed'.format(booking_ID))
        print(booking_Ledger[booking_ID])
        if "parked_Spot_ID" in booking_Ledger[booking_ID]:
            return booking_Ledger[booking_ID]['parked_Spot_ID']
        else:
            return 0