def main():
    milesToKm()

def milesToKm():
    #get miles to be converted to km
    miles = float(input('How many miles do you want converted to kilometers: '))

    count = 1
    while miles < 0 and count < 3:
        print('ERROR: That is not a valid entry')
        miles = float(input('Enter a valid number of miles: '))
        count += 1
    if count == 3 and miles < 0:    
        print('Too many attempts.  Disconnecting')
        exit()
    else:        
    #calculate km/mi
        
        mi_to_km = miles * 1.6
        print('There are', format(mi_to_km, '.2f'), 'kilometers in', miles, 'miles.')


main()
