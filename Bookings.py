import datetime as dt

class Booking:
    Bookings = dict()
    def __init__(self, booking_ID):
        self.booking_ID = booking_ID

    def request_accepted(self, booking_ID):
        '''
        Create a new record using the new bookingID once a booking is confirmed and update it with booking time,
        hold time and status
        :param booking_ID: The booking ID of the new confirmed booking
        '''
        b = Booking
        b.Bookings[booking_ID] = dict()
        b.Bookings[booking_ID]['Booking Time'] = dt.datetime.now()
        b.Bookings[booking_ID]['Hold_Time'] = dt.datetime.now() + dt.timedelta(minutes=10)
        b.Bookings[booking_ID]['booking_Status'] = 'Spot is booked'

        
    def vehicle_Entered(self, booking_ID, car_Licence_Plate_Number):
        '''
        Adds the car_Licence_Plate_Number to the booking record once the vehicle enters the premises
        :param booking_ID: Booking ID of the vehicle that entered
        :param car_Licence_Plate_Number: Licence number of the vehicle that entered
        '''
        b = Booking
        b.Bookings[booking_ID]['entry_Time'] = dt.datetime.now()
        b.Bookings[booking_ID]['car_Licence_Plate_Number'] = car_Licence_Plate_Number
        b.Bookings[booking_ID]['booking_Status'] = 'Vehicle Entered Premises'


    def vehicle_Parked(self, booking_ID, parked_Spot_ID):
        '''
        Adds the parked_Spt_ID to the booking record once the vehicle is parked
        :param booking_ID: Booking ID of the vehicle that is parked
        :param parked_Spot_ID: The spotID where the vehocle is parked
        '''
        b = Booking
        b.Bookings[booking_ID]['parked_Spot_ID'] = parked_Spot_ID
        b.Bookings[booking_ID]['booking_Status'] = 'Vehicle is parked'

    def vehicle_Left(self,booking_ID):
        '''
        Update the status and exit time once the vehicle exits the premises
        :param booking_ID: Booking ID of the vehicle that exited the premises
        '''
        b = Booking
        b.Bookings[booking_ID]['booking_Status'] = 'Vehicle left the premise'
        b.Bookings[booking_ID]['exit_Time'] = dt.datetime.now()

    def get_Bookings(self):
        '''
        Get all the bookings records
        :return: Dictionary containing all the records.
        '''
        b = Booking
        return b.Bookings

    def get_Booking_ID(self, licence_Number):
        '''
        Get the bookingID of the vehicle using the licence_plate_number
        :param licence_Number: The licence_number scanned by any scanner within the premises
        :return: Booking ID associated with the car_Licence_Plate_Number
        '''
        b = Booking
        for book_id in b.Bookings:
            if 'car_Licence_Plate_Number' in b.Bookings[book_id]:
                if b.Bookings[book_id]['car_Licence_Plate_Number'] == licence_Number:
                    booking_ID = book_id
        return booking_ID


