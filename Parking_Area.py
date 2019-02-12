class Parking_Area:
    Parking = dict() #Dictionary to store the details of each spot in the parking lot

    def __init__(self, spot_ID):
        self.spot_ID = spot_ID

    def Parking_dict(self, spot_ID, Available):
        '''
        Function to update the Parkings records based on the spotID and the Availability passed initially
        :param spot_ID: The identification number of the parking spot
        :param Available: Availability of the parking spot (Yes|No)
        :return: Parking dictionary with updated records
        '''
        s = Parking_Area
        s.Parking[spot_ID] = dict()
        s.Parking[spot_ID]['Available'] = Available
        return s.Parking

    def create_Parking_Area(self):
        '''
        Function to create a parking lot in case required.
        :return: New parkings dictionary
        '''
        for i in range(1, 11):
            spot_ID = i
            Available = 1
            s1 = Parking_Area
            new_Parking = s1.Parking_dict(self, spot_ID, Available)
        return new_Parking


    def count_Available_Spots(self,Spots):
        '''
        This function is used to count the number of spots available in the parking area
        :param Spots: Dictionary containing spot IDs and their availability
        :return: It returns the number of available spots in the parking area
        '''

        available_Spots = 0
        for i in Spots:
            if Spots[i]['Available'] == 'Yes':
                available_Spots += 1
        return available_Spots


    def get_Available_Spots(self):
        '''
        This function is used to find the spots that are available in the parking lot
        :return: A list of parking spotIDs that are empty.
        '''
        available_Spots_ID = []
        p1 = Parking_Area
        for i in p1.Parking:
            if p1.Parking[i]['Available'] == 'Yes':
                available_Spots_ID.append(i)
        return available_Spots_ID