miles = float(input('OK Nathan, how many miles do you want converted to kilometers? '))
miles_to_kilometers = miles * 1.6
print('Nathan, there are', format(miles_to_kilometers, '.2f'), 'kilometers for every',\
       miles, 'miles.  Pretty Cool!' )

F = float(input("Give me a temperature in farenheit and I'll convert it to celsius! "))
C = (F - 32) * 5 / 9
print('Got it.  When you convert', F, 'degrees farenheit, you get',\
      format(C, '.1f'), "degrees celsius.  You're welcome!")

gallons = float(input('How many gallons do you have? '))
liters = gallons * 3.9
print('You get', format(liters, '.2f'), 'liters for every', gallons, 'gallons.')

pounds = float(input("Give me a number of pounds and I'll convert them to kilograms: "))
kilograms = pounds * 0.45
print(pounds, 'pounds is equal to', format(kilograms, '.2f'), 'kilograms.  Now you know!')

inches = float(input('Give me a number of inches and I will tell you how many centimeters you have! '))
centimeters = inches * 2.54
print ('You have', format(centimeters, '.2f'), 'centimeters in', inches, 'inches.  Good bye for now!')
               
