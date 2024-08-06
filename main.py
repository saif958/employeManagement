def exit_program():
    print("Exiting the program. Thank you!")
    exit()

def invalid_choice():
    print("Invalid choice. Please try again.")

def menu():
    print("\t\t\t-----------------------------------\t\t\t\t")
    print("\t\t\tWELCOME Employee Management Program\t\t\t\t")
    print("\t\t\t-----------------------------------\t\t\t\t")
    print("\t\t\t       ----PROFILE Manager----     \t\t\t\t")
    print("\n___Please select an option____\n:")
    print("1: Create profile")
    print("2: Read profile")
    print("3: Update profile")
    print("4: Delete profile")
    print("5: Salary check")
    print("6: Age identifier")

switch_dict = {
    1: create,
    2: read,
}
while True:
    menu()
    choice = input("Enter your choice: ").strip()
    choice = int(choice) if choice.isdigit() else None
    action = switch_dict.get(choice, invalid_choice)
    if action:
        action()
    else:
        invalid_choice()
        