# input of miles to kilometers#
miles = float(input('OK Nathan, how many miles do you want converted to kilometers? '))
#calculate km / miles
miles_to_kilometers = miles * 1.6
#output calculated km/mi to user
print('Nathan, there are', format(miles_to_kilometers, '.2f'), 'kilometers for every',\
       miles, 'miles.  Pretty Cool!' )
# get temp in F to be converted to C
F = float(input("Give me a temperature in farenheit and I'll convert it to celsius! "))

#calculate temp in C : (F-32) * 5/9
C = (F - 32) * 5 / 9
#~output calculated temp in C to user
print('Got it.  When you convert', F, 'degrees farenheit, you get',\
      format(C, '.1f'), "degrees celsius.  You're welcome!")
#~input # of gallons to be converted to liters
gallons = float(input('How many gallons do you have? '))
#~calculate # of liters : gallons * 3.9
liters = gallons * 3.9
#~output calculated # of liters to user
print('You get', format(liters, '.2f'), 'liters for every', gallons, 'gallons.')
#~input # of pounds to be converted to kilograms
pounds = float(input("Give me a number of pounds and I'll convert them to kilograms: "))
#~calculate # of kilograms : pounds * 0.45
kilograms = pounds * 0.45
#~output calculated # of pounds to user
print(pounds, 'pounds is equal to', format(kilograms, '.2f'), 'kilograms.  Now you know!')

#~input # inches to be converted to centimeters
inches = float(input('Give me a number of inches and I will tell you how many centimeters you have! '))
#~calculate # of centimeters : inches * 2.54
centimeters = inches * 2.54
#~output calculated # of centimeters to user
print ('You have', format(centimeters, '.2f'), 'centimeters in', inches, 'inches.  Good bye for now!')
               
