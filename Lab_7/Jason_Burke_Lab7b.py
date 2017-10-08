
# This program allows you to input and save student
# names to a file

#set a constant for the number of students
student_no = 12


def main():

    #create an empty list
    students = []
    #create an accumulator and prime the while loop
    count = 0
    
    
    #get the user to add students to the list if they want to
    while count < student_no:
        print('Please enter a student name:')
        stu_name = str(input())

        #append the students list
        students.append(stu_name)
        
        #iterate the accumulator
        count += 1
    #run the edit_list module and pass in the
    #students as an arguement   
    edit_list(students)

    # Open a file to write to 
    outfile = open('names.txt', 'w')

    #write the list to file
    for name in students:
        outfile.write(name + '\n')

    #close the file
    outfile.close()
    #call the read_list function
    print('Here is a list of the contents of the names.txt file:')
    read_list()

   

#define the read list function
def read_list():

    infile = open('names.txt', 'r')

    #read the contents of names.txt to a list
    names_list = infile.readlines()

    # Close the file
    infile.close()

    #strip the \n from each element
    index = 0
    while index < len(names_list):
        names_list[index] = names_list[index].rstrip('\n')
        index += 1

    #print the contents
    print(names_list)
    #convert list to tuple
    names_tuple = tuple(names_list)
    #print (names_tuple)
    

# Define the edit_list function to sort, reverse, append and insert
# data to the file.
def edit_list(stu_list):
    #sort the list alphabetical and then again in reverse order
    stu_list.sort()
    stu_list.reverse()
    # Append the list with the teachers name and insert
    # my name at the beginnig of the list
    stu_list.append('Polanco')
    stu_list.insert(0, 'Burke')
    

    return stu_list
    
    
main()
