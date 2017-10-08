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
    
    # Check to make sure the date entered is a valid date.
    while m < 1 or m > 12 or d < 1 or d > 31 or y != 13:
        print('Error.  That is an invalid date.')
        print('Make sure the year is 2013 and entered'
              ' using only 2 digits.')
        # Call the dates_list function to get new date values.
        m, d, y = dates_list()
    
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

main()
