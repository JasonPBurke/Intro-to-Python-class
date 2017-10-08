# The Student class holds student information.

class Student:
    # The __init__ method initializes the attributes.
    def __init__(self, name, ID, GPA, expected_grade, FT_PT):
        self.__name = name
        self.__ID = ID
        self.__GPA = GPA
        self.__expected_grade = expected_grade
        self.__FT_PT = FT_PT

    # The set_name method sets the student name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_ID method sets the student ID attribute.
    def set_ID(self, ID):
        self.__ID = ID

    # The set_GPA method sets the student GPA attribute.
    def set_GPA(self, GPA):
        self.__GPA = GPA

    # The set_expected_grade method sets the student
    # expected_grade attribute.
    def set_expected_grade(self, expected_grade):
        self.__expected_grade = expected_grade

    # The set_FT_PT method sets the student FT_PT attribute.
    def set_FT_PT(self, FT_PT):
        self.__FT_PT = FT_PT

    # The get_name method gets the student name attribute.
    def get_name(self):
        return self.__name

    # The get_ID method returns the student ID attribute.
    def get_ID(self):
        return self.__ID

    # The get_GPA method returns the student GPA attribute.
    def get_GPA(self):
        return self.__GPA

    # The get_expected_grade method returns the student
    # expected_grade attribute.
    def get_expected_grade(self):
        return self.__expected_grade

    # The get_FT_PT method returns the student FT_PT attribute.
    def get_FT_PT(self):
        return self.__FT_PT

    # The __str__ method returns the objects state
    # as a string.
    def __str__(self):
        return self.__name + \
               "\t\t" + self.__ID + \
               "\t\t" + self.__GPA + \
               "\t\t" + self.__expected_grade + \
               "\t\t  " + self.__FT_PT
