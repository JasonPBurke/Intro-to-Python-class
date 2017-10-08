# This program holds and manages student data.
import student
import pickle

# Global constants for menu choices.
LOOK_UP = 1
ADD = 2
CHANGE_GPA = 3
CHANGE_EXPECTED_GRADE = 4
PRINT_OUT = 5   # To print a tabular output of all student data.
QUIT = 6

# Global constant for the filename.
FILENAME = 'student_info.dat'

# Main function
def main():
    # Load the existing student dictionary
    # and assign it to mystudents.
    mystudents = load_students()

    # Initalize a variable for the user's choice.
    choice = 0

    # Process menu selections until user
    # wants to quit the program.
    while choice != QUIT:
        # Get user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(mystudents)
        elif choice == ADD:
            add(mystudents)
        elif choice == CHANGE_GPA:
            change_GPA(mystudents)
        elif choice == CHANGE_EXPECTED_GRADE:
            change_expected_grade(mystudents)
        elif choice == PRINT_OUT:
            print_out(mystudents)

    # Save the mystudents dictionary to a file.
    save_student(mystudents)
    
# The load_students function opens/creates
# the student_info dictionary.
def load_students():
    try:
        # Open the student_info.dat file
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        student_dict = pickle.load(input_file)

        # Close the student_info.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        student_dict = {}

    # Return the dictionary.
    return student_dict

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('-------------------------------------------')
    print("1. Look up the Student's GPA               |")
    print('2. Add a new student to the class          |')
    print("3. Change a student's GPA                  |")
    print('4. Change the expected grade of a student  |')
    print('5. Print the data for all the students     |')
    print('6. Save and quit the program               |')
    print('-------------------------------------------')
    print()

    # Get the user's choice.
    choice = int(input('Please choose one of the above options: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Pleas enter a valid choice: '))
        
    # Return the user's choice.
    return choice

# The look_up function looks up a student's GPA
# in the specified dictionary and prints it out.
def look_up(mystudents):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in mystudents:
        # Create a variable that points to the instance
        # on the named object that was entered by the user.
        instance = mystudents[name]

        # Call the get_GPA method
        gpa = instance.get_GPA()
        print()
        print(name, "'s GPA is: ", gpa, sep='')
    else:
        print()
        print('That was not a valid name.')
    

# The add function adds a new entry into
# the specified dictionary.
def add(mystudents):
    # Get the student info.
    name = input('Name: ')
    ID = input('Student ID: ')
    GPA = input('Student GPA: ')
    expected_grade = input("Student's Expected Grade: ")
    FT_PT = input('Is student full-time or part-time: ')
    print()
    # Create a Student object named entry.
    entry = student.Student(name, ID, GPA, expected_grade, FT_PT)

    # If a name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in mystudents:
        mystudents[name] = entry
        print()
        print('The student has been added.')
    else:
        print()
        print('That student already exists.')


# The change_GPA function changes the existing
# GPA entry for the specified student.
def change_GPA(mystudents):
    # Get a name to look up.
    name = input("Enter the student's name: ")
    
    if name in mystudents:

        # Retrieve the student object instance based on the
        # student name key.
        instance = mystudents[name]
       
        # Get a new value for GPA.
        print()
        GPA = input('Enter a new GPA for the student: ')
        
        # Set the new GPA value and update dictionary.
        instance.set_GPA(GPA)
        
        print()
        print('Information updated.')
    else:
        print()
        print('That name was not found.')

# The change_expected_grade function changes the existing
# expected_grade entry for the specified student.
def change_expected_grade(mystudents):
    # Get a name to look up
    name = input("Enter the student's name: ")

    if name in mystudents:
        # Set up a pointer to the data using the name as a key.
        instance = mystudents[name]
        
        # Get a new value for expected_grade.
        print()
        expected_grade = input('Enter the expected grade for the student: ')

        # Update the entry.
        instance.set_expected_grade(expected_grade)
        print()
        print('Information updated.')
    else:
        print()
        print('That name was not found.')

# The print_out function prints out the data of all the
# students in a tabular format.
def print_out(mystudents):
    print()
    print('------------------------------------------------------------------------------')
    print('Name\t\tStudent ID\tGPA\t\tExpected Grade\t  FT\PT Status')
    print('------------------------------------------------------------------------------')
    # Print out all the student data in a tabular format.
    for name in mystudents:
        print(mystudents.get(name), '\n')
        
    print('------------------------------------------------------------------------------')        
# The save_student function pickles the specified
# object and saves it to the contacts file.
def save_student(mystudents):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mystudents, output_file)

    # Close the file.
    output_file.close()


# Call main
main()
