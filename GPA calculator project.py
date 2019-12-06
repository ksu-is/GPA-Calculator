#using the pip install command, install pandas into pyhton using the 'pip install pandas' command in the terminal
#Then we import pandas at the beginning
import pandas as pd
#Initialize both the current hours and GPA earned for the student as number variables. 
#Even if the student does not enter the numbers, these variables will still work with zeroes for final calculation
current_hours = 0.00
current_gpa = 0.00

#Initialize lists for program of inputting the semester hours and grades
semester_class = []
semester_hours = []
semester_grades = []

#Semester grades program that loops while user enters in their current semester classes and expected grades until they're finished.
def SemesterGrades(semester_class,semester_hours,semester_grades):
    while True:
        class_input = input("Enter the name of your class: ")
        while class_input:
            if class_input.isalnum() == False:
                print("Invalid Entry.")
                class_input = input("Enter the name of your class: ")
            else:
                semester_class.append(class_input)
                break
        hours_input = input("Enter the number of hours for the class: ")
        while hours_input:
            if hours_input.isdigit() == False:
                print("Invalid Entry")
                hours_input = input("Enter the number of hours for the class: ")
            else:
                semester_hours.append(hours_input)
                break
        grade_input = input("Enter your expected letter grade for the class (A, B, C, D, or F): ")
        while grade_input:
            if grade_input.upper() == "A":
                semester_grades.append("4")
                break
            elif grade_input.upper() == "B":
                semester_grades.append("3")
                break
            elif grade_input.upper() == "C":
                semester_grades.append("2")
                break
            elif grade_input.upper() == "D":
                semester_grades.append("1")
                break
            elif grade_input.upper() == "F":
                semester_grades.append("0")
                break
            else:
                print("Invalid Entry")
                grade_input = input("Enter your expected letter grade for the class (A, B, C, D, or F): ")
        add_classes = input("Would you like to add another class? ")
        if add_classes.lower().startswith("n") == True:
            break
        else:
            pass

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
            if float(current_gpa_entry) > 4:
                print("Invalid entry")
                current_gpa_entry = input("Enter your total earned GPA: ")
            elif current_gpa_entry.isalpha() == False:
                current_gpa = float(current_gpa_entry)
                break
            else:
               print("Invalid entry")
               current_gpa_entry = input("Enter your total earned GPA: ")
        break
    else:
        break

#Print the entries by the user
print("Current hours:",current_hours)
print("Current GPA:", current_gpa)
print()
print("Enter your current classes, hours and expected grades.")
SemesterGrades(semester_class,semester_hours,semester_grades)

#Now that we have gathered current and semester hours and grades, we will calculate the final GPA
#Add current hours to total hours
total_hours = current_hours
#Add the hours for each class to the total hours
for num in semester_hours:
    total_hours += float(num)
#Initialize the weight of current hours to total_gpa variable
total_gpa = current_hours * current_gpa
#Now include the weight of each class entered to total_gpa variable
for num in range(0,len(semester_hours)):
    total_gpa += float(semester_hours[num]) * float(semester_grades[num])
#Divide total_gpa variable by the total hours to get the overall expected GPA including current semester grades
total_gpa = total_gpa / total_hours
print("Total hours:",total_hours)
print("Total Expected GPA:",total_gpa)
print()
excel_export_decision = input("Would you like to export the information to an Excel file? ")
if excel_export_decision.lower().startswith('y') == True:
    raw_data = {'Current Hours': [current_hours],
    'Current GPA': [current_gpa],
    'Class Name': [semester_class],
    'Class Hours': [semester_hours],
    'Class GPA': [semester_grades],
    'Overall Hours': [total_hours],
    'Overall GPA': [total_gpa]}
    df= pd.DataFrame(raw_data,columns= ['Current Hours','Current GPA','Class Name','Class Hours','Class GPA','Overall Hours','Overall GPA'])
    export_excel = df.to_excel (r'C:\Users\harol\Desktop\export_dataframe.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path and change it to a local path on your machine
    print(df)
    print("Thank you for using the GPA Calculator!")
else:
    print("Thank you for using the GPA Calculator!")