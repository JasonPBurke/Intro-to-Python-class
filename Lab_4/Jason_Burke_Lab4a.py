
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


# get temp in F to be converted to C
F = float(input("Give me a temperature in farenheit and I'll convert it to celsius: "))

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
#calculate temp in C : (F-32) * 5/9
    C = (F - 32) * 5 / 9              
    print('Got it.  When you convert', F, 'degrees farenheit, you get',\
          format(C, '.1f'), "degrees celsius.")


#~input # of gallons to be converted to liters
gallons = float(input('How many gallons do you have? '))

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
#~calculate # of liters : gallons * 3.9
    liters = gallons * 3.9
    print('You get', format(liters, '.2f'), 'liters for every', gallons, 'gallons.')


#~input # of pounds to be converted to kilograms
pounds = float(input("Give me a number of pounds and I'll convert them to kilograms: "))

count = 1
while pounds < 0 and count < 3:
    print('ERROR: Not a valid weight.')
    pounds = float(input('Enter a valid weight: '))
    count += 1
if count == 3 and pounds < 0:
    print('Too many attempts made.  Disconnecting.')
    exit()
else:
#check not negitave and calculate # of kilograms : pounds * 0.45
    kilograms = pounds * 0.4
    print(pounds, 'pounds is equal to', format(kilograms, '.2f'), 'kilograms.'\
          'Now you know!')


#~input number of inches to be converted to centimeters
inches = float(input('Give me a number of inches and I will tell you' \
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
#~calculate # of centimeters : inches * 2.54
    centimeters = inches * 2.5
    print ('You have', format(centimeters, '.2f'), 'centimeters in', inches, \
           'inches.  Good bye for now!')
