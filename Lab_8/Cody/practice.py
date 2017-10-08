def main():

    print('Hello and welcome to the calendar converter!')
    date = input('Please enter a date in the format of mm/dd/yy: ')
        
    time = date.split('/')
        
    month = int(time[0])
    day = int(time[1])
    year = int(time[2])
    print(month, day, year)

    flag = False
    while flag == False:
        if month < 1 or month > 12:
            date = input('The date entered was incorrect.'
                         'please enter the date again: ')
            time = date.split('/')
        
            month = int(time[0])
            day = int(time[1])
            year = int(time[2])
            
            print(month, day, year)
            
        elif day < 1 or day > 31:
            date = input('The date entered was incorrect.'
                         'please enter the date again: ')
            time = date.split('/')
        
            month = int(time[0])
            day = int(time[1])
            year = int(time[2])
            
        elif year != 13:
            date = input('The date entered was incorrect.'
                         'please enter the date again: ')
            time = date.split('/')
        
            month = int(time[0])
            day = int(time[1])
            year = int(time[2])
            print(month, day, year)
        else:
            flag = True
            

    if month == '01':
        month = 'January'
    elif month == '02':
        month = 'February'
    elif month == '03':
        month = 'March'
    elif month == '04':
        month = 'April'
    elif month == '05':
        month = 'May'
    elif month == '06':
        month = 'June'
    elif month == '07':
        month = 'July'
    elif month == '08':
        month = 'August'
    elif month == '09':
        month = 'September'
    elif month == '10':
        month = 'October'
    elif month == '11':
        month = 'November'
    elif month == 12:
        month = 'December'


    print(month, day, year)





main()
