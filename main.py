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
    print("5: younger employee identify")
    print("6: Address check")
    print("7: salary check")
    print("8: longest name check")
    print("9: Age maximum and minimumcheck")
    print("10: exit")
def invalid_choice():
    print("Invalid choice. Please try again.")
switch_dict = {
1:create_profile,
2:read,
3:update_profile,
4:delete_profile,
5:age_identifier,
6:adrress_locate,
7:salary,
8:name,
9:age,
10:exit_menu
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
