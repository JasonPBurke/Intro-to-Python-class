

def main():
    #store filename as a variable
    grades_path = 'grades.txt'
    #open a file to be written to
    outfile = open(grades_path, 'w')

    total_students = 1
    while total_students <= 3:
        stu_name = str(input('Enter the students name: '))
        #write name to file
        outfile.write(stu_name + '\n')
        valid = False
        
        while valid == False:
        
            try:
                
                avg_grade = float(input('Enter the student average grade: '))

                if avg_grade < 0 or avg_grade > 100:
                    raise ValueError('Error: Grade average cannot be greater than' + \
                                     '100 or less than 0.')
                #write to file
                outfile.write(str(avg_grade) + '\n')
                valid = True
            
            #print the exception
            except Exception as err:
                print(err)
        #increment students        
        total_students += 1        
    #close the file
    outfile.close()

    valid = False
    input_path = grades_path
    while not valid:
        try:
            #open the grades.txt file
            infile = open(input_path, 'r')
        except Exception as err:
            print(err)
            print('Bad Filename. Please enter a valid filename to continue.')
            input_path = input('Enter a new filename: ')
    name = infile.readline()
    
    while line != '':

        name  = str(infile.readline())

        line = line.rstrip('\n')
        
        print('Name:', name)
        print('Grade:', line)
        line =infile.readline()
# run the main method
main()
