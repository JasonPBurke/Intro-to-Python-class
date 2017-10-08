# This program will allow a user to enter a date in
# numeric format.  It will test the month, day, and
# year and have the user correct if errors are found.
# It will then output the date in long date format.

# Import the calander module to assist with renaming
# months entered by the user.
import calendar

def main():

    # Call the dates_list function to get date element values.
    m, d, y  = dates_list()
    
    m, d, y = check_dates(m, d, y)
            
    # Define the numerical month and assign a month name.
    month = calendar.month_name[m]
    
    # Return to user the date entered in long date format.
    print('The date you entered is ', month, ' ', d, ', ', '20', y, '.', sep='')


# Create a function to split the date and rename the
# list elements.
def dates_list():
    
    # Get a date from the user in numeric format
    user_date = input('Please enter a date in mm/dd/yy format: ')

    # Split up the day, month, and year from user_date into a list.
    date_list = user_date.split('/')
    
    # Rename the list elements
    m = int(date_list[0])
    d = int(date_list[1])
    y = int(date_list[2])

    return (m, d, y)
def date_error():
        print('Error.  That is an invalid date.')
        print('Make sure the year is 2013 and entered'
              ' using only 2 digits.')
        # Call the dates_list function to get new date values.
        #m, d, y = dates_list()

"""check_dates int: m,d,y in: 2, 31, 13 (0)
      check_dates in:02, 35, 92 (b)
          check_date3 in: 01, 01, 13 (e)
"""

def check_dates(m,d,y): #(0)
        # Check to make sure the date entered is a valid date. (c, f)
    while m < 1 or m > 12 or d < 1 or d > 31 or y != 13:
        date_error()
        m, d, y = dates_list() # (d) out: 01, 01, 13
        print(m,d,y)
        m, d, y = check_dates(m,d,y) # (e) in:01, 01, 13; out: trashed
    # Check individual months for correct
    #number of days using for loops.
    while m in [4,6,9,11]:
        if d > 30:
            date_error()
            # Call the dates_list function to get new date values.
            m, d, y = dates_list()
            m , d, y = check_dates(m,d,y)
    # m == last from dates_list() always
    while m in [2,]:
        if d > 29:
            date_error()
            # Call the dates_list function to get new date values.
            m, d, y = dates_list() # (a) out: 2, 35, 91
            # 3 + 3
            # res = 3+3
            m, d, y = check_dates(m,d,y) #2, 35, 91 (b)->(g)
    return(m,d,y)
main()
