
#define miles to km function
def MilesToKm():

    try:
        # open a file to be written to
        outfile = open('conversions.txt', 'a')
        
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
            #write starting values to conversions.txt file
            outfile.write (str(miles) + '\n')
            outfile.write('Miles' + '\n')
            #calculate km/mi
            mi_to_km = miles * 1.6
            result = print('\nThere are', format(mi_to_km, '.2f'), 'kilometers in', miles, 'miles.\n')
            #write converted values to conversions.
            outfile.write(str(mi_to_km) + '\n')
            outfile.write('Kilometers' + '\n')
            return result
    except:
        print('An error has occured.\n')
    #close the file
    outfile.close()

    
#define temp conversion function
def FahToCel():
    try:
        # open a file to be written to
        outfile = open('conversions.txt', 'a')
        # get temp in F to be converted to C
        F = float(input("\nGive me a temperature in farenheit and I'll convert it to celsius: "))

        #check temp range and output calculated temp in C to user
        count = 1
        while F > 1000 and count < 3:
            print('ERROR: Not a valid temp.')
            F = float(input('Enter a valid temp: '))
            count += 1
        if count == 3 and F > 1000:
            print('Too many attempts. Disconnecting.')
            exit()
        else:
            #write starting values to conversions.txt file
            outfile.write (str(F) + '\n')
            outfile.write('Farenheit' + '\n') 
            #calculate temp in C : (F-32) * 5/9
            C = (F - 32) * 5 / 9              
            result = print('\nGot it.  When you convert', F, 'degrees farenheit, you get\n',\
                  format(C, '.1f'), "degrees celsius.\n")
            #write converted values to conversions.
            outfile.write(str(C) + '\n')
            outfile.write('Celsius' + '\n')
            return result
    except:
        print('An error has occured\n')
        
    #close the file
    outfile.close()
        
#define gallons to liters function
def GalToLit():
    try:
        # open a file to be written to
        outfile = open('conversions.txt', 'a')
        #~input # of gallons to be converted to liters
        gallons = float(input('\nHow many gallons do you have? '))

        #~output calculated # of liters to user and check valid weight
        count = 1
        while gallons < 0 and count < 3:
            print('ERROR: Not a valid weight')
            gallons = float(input('Enter a valid weight: '))
            count += 1
        if count == 3 and gallons < 0:
            print('Too many attempts. Disconnecting.')
            exit()
        else:
            #write starting values to conversions.txt file
            outfile.write (str(gallons) + '\n')
            outfile.write('Gallons' + '\n') 
            #~calculate # of liters : gallons * 3.9
            liters = gallons * 3.9
            result = print('\nYou get', format(liters, '.2f'), 'liters for every', gallons, 'gallons.\n')
            #write converted values to conversions.
            outfile.write(str(liters) + '\n')
            outfile.write('Liters' + '\n')
            return result
    except:
        print('An error has occured\n')
        
    #close the file
    outfile.close()
        
#Define weight conversion function
def PoundsToKg():
    try:
        # open a file to be written to
        outfile = open('conversions.txt', 'a')
        #~input # of pounds to be converted to kilograms
        pounds = float(input("\nGive me a number of pounds and I'll convert them to kilograms: "))

        count = 1
        while pounds < 0 and count < 3:
            print('ERROR: Not a valid weight.')
            pounds = float(input('Enter a valid weight: '))
            count += 1
        if count == 3 and pounds < 0:
            print('Too many attempts made.  Disconnecting.')
            exit()
        else:
            #write starting values to conversions.txt file
            outfile.write (str(pounds) + '\n')
            outfile.write('Pounds' + '\n')  
            #check not negitave and calculate # of kilograms : pounds * 0.45
            kilograms = pounds * 0.4
            result = print('\nYour',pounds, 'pounds is equal to', format(kilograms, '.2f'), 'kilograms.  '\
                  'Now you know!\n')
            #write converted values to conversions.
            outfile.write(str(liters) + '\n')
            outfile.write('Liters' + '\n')
            return result
    except:
        print('An error has occured\n')
        
    #close the file
    outfile.close()
    
#define inches to cm conversion function
def InchesToCm():
    try:
        # open a file to be written to
        outfile = open('conversions.txt', 'a')
        #~input number of inches to be converted to centimeters
        inches = float(input('\nGive me a number of inches and I will tell you ' \
                             'how many centimeters you have. '))

        count = 1
        while inches < 0 and count < 3:
            print('ERROR: Not a valid entry.')
            inches = float(input('Enter a valid length of inches: '))
            count += 1
        if count == 3 and inches < 0:
            print('Too many attempts.  Disconnecting.')
            exit()
        else:
            #write starting values to conversions.txt file
            outfile.write (str(inches) + '\n')
            outfile.write('Inches' + '\n')  
        #~calculate # of centimeters : inches * 2.54
            centimeters = inches * 2.5
            result = print ('\nYou have', format(centimeters, '.2f'), 'centimeters in', inches, \
                   'inches.\n')
            #write converted values to conversions.
            outfile.write(str(centimeters) + '\n')
            outfile.write('Centimeters' + '\n')
            return result

    except:
        print('An error has occured\n')
        
    #close the file
    outfile.close()
