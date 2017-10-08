#import external function module
import Jason_Burke_Lab6aa

#define main function
def main():

    try:

        print("Hello there!  I'm here to make conversions for you.")
        
        #count total number of conversions and stop at 10
        total_conversions = 1 
        while total_conversions <= 10:
            print("Here's a list of what I can convert:")
            print('A) Miles to Kilometers\n' + \
                  'B) Gallons to Liters\n' + \
                  'C) Pounds to Kilograms\n' + \
                  'D) Inches to Centimeters\n' + \
                  'E) Farenheit to Celsius\n')
            choice = str(input('Tell me what to convert and I will convert it!\n' + \
                                '(ex. enter "B" to convert gallons to liters)\n'+ \
                               'Enter the letter now to pick a conversion: '))
            total_conversions +=1
            
            #call the function chosen by the user
            if choice == 'a' or choice == 'A':
                Jason_Burke_Lab6aa.MilesToKm()
            elif choice == 'b' or choice == 'B':
                Jason_Burke_Lab6aa.GalToLit()
            elif choice == 'c' or choice == 'C':
                Jason_Burke_Lab6aa.PoundsToKg()
            elif choice == 'd' or choice == 'D':
                Jason_Burke_Lab6aa.InchesToCm()
            elif choice == 'e' or choice == 'E':
                Jason_Burke_Lab6aa.FahToCel()
            else:
                raise ValueError('An ERROR has occured. Shutting down.')
                
    except Exception as err:
                print(err)

    
#call main function
main()
                 
