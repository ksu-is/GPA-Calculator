#Initialize both the current hours and GPA earned for the student as number variables. 
#Even if the student does not enter the numbers, these variables will still work with zeroes for final calculation
current_hours = 0.00
current_gpa = 0.00

#Initialize lists for program of inputting the semester hours and grades
semester_hours = []
semester_gpa = []

#Semester grades program that loops while user enters in their current semester classes and expected grades until they're finished.
#def SemesterGrades():
    #while True:
        #break

#Greet the user and ask if they would like to add their current earned GPA and total credit hours
print("Welcome to the GPA Calculator program!")
initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No) ")
while initial_option:
    if initial_option.isalpha() == False:
        print("Invalid entry")
        initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No) ")
    elif initial_option.lower().startswith('y'):
        current_hours_entry = input("Enter your total earned hours: ")
        while current_hours_entry:
            if current_hours_entry.isnumeric() == True:
                current_hours = float(current_hours_entry)
                break
            else:
               print("Invalid entry")
               current_hours_entry = input("Enter your total earned hours: ")
        current_gpa_entry = input("Enter your total earned GPA: ")
        while current_gpa_entry:
            if current_gpa_entry.isalpha() == False:
                current_gpa = current_gpa_entry
                break
            else:
               print("Invalid entry")
               current_gpa_entry = input("Enter your total earned GPA: ")
        break
    else:
        break

#Print the entries by the user
while current_hours > 0:
    print("Current hours:",current_hours)
    print("Current GPA:", current_gpa)
#Verify they input the numbers correctly, if yes then break otherwise they can re-enter the names
    current_validation = input("Were the current numbers entered correctly? (Yes/No)")
    while current_validation:
        if current_validation.isalpha() == False:
            print("Invalid entry")
            current_validation = input("Were the current numbers entered correctly? (Yes/No)")
        elif current_validation.lower().startswith('y'):
            break
        else:
            current_hours_entry = input("Enter your total earned hours: ")
            while current_hours_entry:
                if current_hours_entry.isalpha() == False:
                    current_hours = float(current_hours_entry)
                    break
                else:
                    print("Invalid entry")
                    current_hours_entry = input("Enter your total earned hours: ")
            current_gpa_entry = input("Enter your total earned GPA: ")
            while current_gpa_entry:
                if current_gpa_entry.isalpha() == False:
                    current_gpa = float(current_gpa_entry)
                    break
                else:
                    print("Invalid entry")
                    current_gpa_entry = input("Enter your total earned GPA: ")
            print("Current hours:",current_hours)
            print("Current GPA:", current_gpa)
            current_validation = input("Were the current numbers entered correctly? (Yes/No)")