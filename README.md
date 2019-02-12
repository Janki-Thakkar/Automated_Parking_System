# Automated_Parking_System

This program is designed to accept customer requests and book parking spots.
Once a vehicle enters the parking lot, license number is scanned and uploaded to all the records.
The licence number is then used to scan the activities of the vehicle such as parking and exit from the premises.


Assumptions:
In this program, I have assumed that there are 10 parking spots (this can be changed) and at the beginning all of them are empty.
The server handles one request at a time. I have created a server object separately so that multiple servers can be created in later
stage.
The customer is aware of the parking structure and chooses a his/her own parking spot.
The license plate number is scanned at the entrance as well as the parking spot to update the records for a particular booking.
The count of available spots decreases when a new booking is made but the availability of a parking spot changes only when a park
request is raised by the customer (parking spot is chosen by the customer)
The entry point to the system is only through raising a request for booking a spot.
