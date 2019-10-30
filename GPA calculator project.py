def current_grades():

def semester_grades():

def main():

initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No)")

while initial_option:
    if initial_option.alpha() == False:
        print("Invalid entry")
        initial_option = input("Would you like to enter your current GPA and credit hour totals? ")
    elif initial_option.lower().startswith() == 'y':
        current_grades()
        break
    else:
        break

