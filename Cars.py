import random

class Car:
    def __init__(self, booking_ID):
        self.ID = booking_ID

    def licence_plate_number(self):
        '''
        Function to randomly generate a car_lincence_Plate_Number in a particular pattern
        :return: Randomly generated car_lincence_Plate_Number
        '''
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        D1 = random.choice(letters)
        D2 = random.choice(letters)
        D3 = random.choice(letters)
        D4 = random.choice(numbers)
        D5 = random.choice(numbers)
        D6 = random.choice(numbers)
        D7 = random.choice(numbers)

        return(D1+D2+D3+'-'+D4+D5+D6+D7)
