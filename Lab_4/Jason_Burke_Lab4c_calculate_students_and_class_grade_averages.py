#this program discovers the number of students in a class
#and then allows students to enter any number of test scores
#while keping track of how many test scores were entered
#it will convert average score to a letter grade and end when
#user prompts that there are no more test scores to enter

#collect number of students in class
num_students = int(input('How many students do you have? '))

#starting with the first student, get test scores
#show letter grade and give a statement on grade, then
#go to next student when first student enters grade of -1(sentinel)
#and repeat above process (use for loop with range = num_students
#test_totals  = 0
#test_score   = 0
#num_of_tests = 0
total_class_tests = 0
class_test_total = 0
for student in range (num_students):
    test_totals  = 0
    test_score   = 0
    num_of_tests = 0
    #total_class_tests = 0
    #class_test_total = 0
    if student > 0:
        print('\nNext Student:')
    test_score = float(input('Enter your test score or enter -1 if done: '))
    while test_score != -1:
        test_totals += test_score
        num_of_tests += 1
        total_class_tests += 1
        class_test_total += test_score

        if test_score > 100:
            print('\nTest Score: ', format(test_score, '.1f'), 'Great job on the extra credit. A++.') 
        if test_score <= 100 and test_score >= 90:
            print('\nTest Score:', format(test_score, '.1f'), 'You got an A on the test.'
                  '  Great Job!')
        elif test_score <=89 and test_score >= 80:
            print('\nTest Score:', format(test_score, '.1f'), 'You got a B on the test.'
                  '  Pretty good!')
        elif test_score <=79 and test_score >= 70:
            print('\nTest Score:', format(test_score, '.1f'), 'You got a C on the test.'
                  '  Gotta study a bit harder!')
        elif test_score <=69 and test_score >= 60:
            print('\nTest Score:', format(test_score, '.1f'), 'You got a D on the test.'
                  '  Step it up!!!')
        elif test_score <= 59 and test_score >= 0:
            print('\nTest Score:', format(test_score, '.1f'), 'You got an F on the test.'
                  '  You must study to pass!!!')
        test_score = float(input('Enter another test score or enter -1 if done: '))

#average a students grades and print out a message
    average_grade = 0
    if num_of_tests == 0:
        print('No test numbers given')
    else:
        average_grade = test_totals / num_of_tests
    if average_grade <= 100 and average_grade >= 90:
        print('\nGrade Average:', format(average_grade, '.1f'), 'You have an A in the class.'
              '  Great Job!')
    elif average_grade <=89 and average_grade >= 80:
        print('\nGrade Average:', format(average_grade, '.1f'), 'You have a B in the class.'
              '  Pretty good!')
    elif average_grade <=79 and average_grade >= 70:
        print('\nGrade Average:', format(average_grade, '.1f'), 'You have a C in the class.'
              '  Gotta study a bit harder!')
    elif average_grade <=69 and average_grade >= 60:
        print('\nGrade Average:', format(average_grade, '.1f'), 'You have a D in the class.'
              '  Step it up!!!')
    elif average_grade <= 59 and average_grade >= 0:
        print('\nGrade Average:', format(average_grade, '.1f'), 'You have an F in the class.'
              '  You must study to pass!!!')

#calculate the class average
if total_class_tests == 0:
    print('\nNo class test scores provided.')
    
else:
    class_avg = class_test_total / total_class_tests
    print('\nUsing ', total_class_tests, ' test(s), The Class Average is: ', format(class_avg, '.1f'), '.  How do you stack up?', sep='')

exit = input("\npress enter to exit program")
