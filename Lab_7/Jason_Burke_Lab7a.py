#create a table using a two dimentional list that stores
#a fahrenheit temperature and the equivalent Celcius temp



def main():

    #call different lists with their own values stored in it
    temp = get_temps()
    distance = get_distance()
    volume = get_volume()
    weight = get_weight()
    length = get_length()
    
    #Display the contents of the list
    print('Here are all the temp conversions from C to F in the list:')
    print(temp)
    print('')
    print('Here are all the distance conversions from Mi to Km in the list:') 
    print(distance)
    print('')
    print('Here are all the volume conversions from Gal to Lt in the list:')
    print(volume)
    print('')
    print('Here are all the weight conversions from Lb to Kilo in the list:')
    print(weight)
    print('')
    print('Here are all the length conversions from In to Cm in the list:')
    print(length)
    
#the get_temps function converts a range of temps
#to their Celcius equivilant and returns a refrence to the list
def get_temps():
    #create an empty list
    temp_conversions = []
    

    #fill the list with data from the conversion equasion
    #using a for loop
    for F in range(-10, 101, 10):
        C = round((F - 32) * 5 / 9, 1)
    
        temp_conversions.append([F, C])
        
    return temp_conversions


#convert the distances and return the values to a list
def get_distance():
    #create an empty list
    distance_conversions = []

    #use a for loop to populate the list with start/end
    #conversion values
    for M in range(0, 101, 10):
        Km = M * 1.6
        distance_conversions.append([M, Km])
           
    return distance_conversions

#convert gallons to liiters and return values to the list
def get_volume():
    #start with an empty list
    volume_conversions = []

    #using a for loop to populate the list in 2d format
    for Gal in range(0, 101, 10):
        Lit = Gal * 3.9
        volume_conversions.append([Gal, Lit])

    return volume_conversions

#convert weight and return values to the list
def get_weight():
    #create an empty list
    weight_conversions = []

    #use a for loop to populate the list
    for Lbs in range(0, 101, 10):
        Kilo = Lbs * 0.45
        weight_conversions.append([Lbs, Kilo])

    return weight_conversions

#convert length and return values to a list
def get_length():
    #create an empty list
    length_conversions = []

    #populate the empty list using a for loop and a range
    for In in range(0, 101, 10):
        Cm = In * 2.54
        length_conversions.append([In, Cm])

    return length_conversions

#call main
main()
