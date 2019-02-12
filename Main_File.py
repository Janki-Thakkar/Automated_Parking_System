'''
Assumptions:
In this program, I have assumed that there are 10 parking spots (this can be changed) and at the beginning all of them are empty.
The server handles one request at a time. I have created a server object separately so that multiple servers can be created in later
stage.
The customer is aware of the parking structure and chooses a his/her own parking spot.
The license plate number is scanned at the entrance as well as the parking spot to update the records for a particular booking.
The count of available spots decreases when a new booking is made but the availability of a parking spot changes only when a park
request is raised by the customer (parking spot is chosen by the customer)
The entry point to the system is only through raising a request for booking a spot.
'''

from Server import Server
from Customer import Customer
from Parking_Area import Parking_Area
from Bookings import Booking
import random, time

##Create a parking area with 10 parking spots. The spot ID and availability of the parking spot is stored in the dictionary Parking_Lot
Parking_Lot = dict()
for i in range(1,11):
    spot_ID = i
    Available = 'Yes'
    s1 = Parking_Area(spot_ID)
    Parking_Lot = s1.Parking_dict(spot_ID, Available)
#print(Parking_Lot)
p1 = Parking_Area(1)
print("Parking Lot with 10 parking spots created")
available_Spots = p1.count_Available_Spots(Parking_Lot)
print("Available spots:",available_Spots)
available_Spot_ID = p1.get_Available_Spots()


bookings_List = []  #A list to store all the booking IDs when the booking is made
entered_Bookings_List = [] #List to store the booking IDs that have entered the parking lot
parked_Cars_List = [] #List to store the license number of the cars that are parked
entered_Cars_List = [] #List to store the license number of the cars that have entered the premises

def handleRequests(requestType):
    '''
    This function handles all types of requests raised by the customers. The types of requests handled are: New booking,
    Enter the premises, Park the car and Exit the premises
    :param requestType: It is the type of request raised by customer
    :return: Returns nothing. Prints the processing happening in each request
    '''
    global available_Spots #Spots available in the parking lot
    print("{} request received.".format(requestType))
    response = ''
    s1 = Server(1) #Creating a server object
    c1 = Customer(random.randint(1, 99)) #Creating a random Customer object
    #Cases to handle various requests
    if requestType == 'New':
        c1.raise_Request(c1.customer_ID)  #Customer raises a request
        ser_response = s1.request_Response(c1.customer_ID, available_Spots)  #Server responds to the customer request
        if ser_response == 'Y':  #If parking is available, customer is asked to confirm request
            response = c1.confirm_Request(c1.customer_ID)
            print(response)
            # Booking is created if the customer confirms the request and the count to available_Spots is updated
            booking_ID, avail_Spots_New = s1.create_Booking(response, available_Spots)
            available_Spots = avail_Spots_New
            #If a booking is created then the booking ID is added to the bookings_List and a confirmation is sent to customer
            if booking_ID != 0:
                bookings_List.append(booking_ID)
                c1.receive_Confirmation(booking_ID)
            print("Available spots:",available_Spots)
            print(Parking_Lot)

    elif requestType == 'Entry':
        booking_ID = random.choice(bookings_List) #A random booking ID is chosen to raise a request for entry
        c1.raise_Entry_Request(booking_ID) #Using the random booking_ID, customer request is generated
        #Booking is sent for verification to the server
        licence_Number = s1.verifyBooking(booking_ID)
        c1.update_Licence_Plate(booking_ID, licence_Number) #The license plate is updated on the customer record
        #Once vehicle enters, the entered_Bookings_List, entered_Cars_List and bookings_List are updated
        entered_Bookings_List.append(booking_ID)
        entered_Cars_List.append(licence_Number)
        bookings_List.remove(booking_ID)
        print("Available spots:",available_Spots)
        print(Parking_Lot)

    elif requestType == 'Park':
        entered_Booking_ID = random.choice(entered_Bookings_List) #A random booking ID is chosen from entered cars to park
        b = Booking(entered_Booking_ID)
        #Customer scans available spots and parks in a spot. The licence_number is scanned at the parking spot
        booked_Spot, licence_Number = c1.park_Car(entered_Booking_ID, available_Spot_ID)
        #Booking ledger is updated using the licence number scanned by the parking spot
        booking_ID = b.get_Booking_ID(licence_Number)
        s1.update_Records(booking_ID, booked_Spot)
        #Spot availability is updated.
        Parking_Lot[booked_Spot]['Available'] = 'No'
        #All the lists except bookings_List are updated
        parked_Cars_List.append(b.Bookings[entered_Booking_ID]['car_Licence_Plate_Number'])
        entered_Cars_List.remove(b.Bookings[entered_Booking_ID]['car_Licence_Plate_Number'])
        entered_Bookings_List.remove(entered_Booking_ID)
        print("Available spots:",available_Spots)
        print(Parking_Lot)

    else:
        #A random licence number is chosen from parked and entered cars list.
        #Entered cars list is considered as a customer may need to leave without parking.
        #For exit, the licence number is scanned when a car moves from the parking spot and goes through the exit gate
        parked_Entered_List = list(set(parked_Cars_List+entered_Cars_List))
        exit_Licence_Number = random.choice(parked_Entered_List)
        b = Booking(exit_Licence_Number)
        car_number = c1.exit_Premises(exit_Licence_Number) #Customer exits the premises and licence number is scanned
        #All the lists are updated with the booking_ID/car_Licence_Plate_Number
        exit_booking_ID = b.get_Booking_ID(car_number)
        available_Spots += 1
        vacated_Spot = s1.endBooking(exit_booking_ID)
        if vacated_Spot != 0:
            print('Spot empty:', vacated_Spot)
            Parking_Lot[vacated_Spot]['Available'] = 'Yes'
        if exit_Licence_Number in parked_Cars_List:
            parked_Cars_List.remove(exit_Licence_Number)
        else:
            entered_Cars_List.remove(exit_Licence_Number)
            entered_Bookings_List.remove(exit_booking_ID)
        print("Available spots:",available_Spots)
        print(Parking_Lot)


if __name__ == '__main__':
    #20 random requests are genrated based on the values in the lists.
    for i in range(20):
        print("=============================================================================================================")
        if (bookings_List) and (entered_Bookings_List) and (parked_Cars_List):
            options = ['New', 'Entry', 'Park', 'Exit']
        elif (bookings_List) and (entered_Bookings_List) and (not parked_Cars_List):
            options = ['New', 'Entry', 'Park', 'Exit']
        elif (bookings_List) and (not entered_Bookings_List) and (parked_Cars_List):
            options = ['New', 'Entry', 'Exit']
        elif (bookings_List) and (not entered_Bookings_List) and (not parked_Cars_List):
            options = ['New', 'Entry']
        elif (not bookings_List) and (entered_Bookings_List) and (parked_Cars_List):
            options = ['New', 'Park', 'Exit']
        elif (not bookings_List) and (entered_Bookings_List) and (not parked_Cars_List):
            options = ['New', 'Park', 'Exit']
        elif (not bookings_List) and (not entered_Bookings_List) and (parked_Cars_List):
            options = ['New', 'Exit']
        else:
            options = ['New']

        handleRequests(random.choice(options))