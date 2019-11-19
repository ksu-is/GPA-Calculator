initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No)")
current_hours = 0
current_gpa = 0

while initial_option:
    if initial_option.isalpha() == False:
        print("Invalid entry")
        initial_option = input("Would you like to enter your current GPA and credit hour totals? ")
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

print(current_hours, current_gpa)