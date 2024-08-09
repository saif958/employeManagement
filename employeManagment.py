employee_data = {}
emp_id = 1
def create_profile():
    global employee_data, emp_id
    while True:
        print(f"{len(employee_data) + 1}")
        name = input("Enter employee name :")
        location = input(str("Enter employee location :"))
        salary = input("Enter employee salary :")  
        age = int(input("Enter employee age :"))

        employee_dict = {
            "name": name,
            "age": age,
            "location": location,
            "salary": salary
        }
        employee_data[emp_id] = employee_dict
        print("Employee added:")
        print(f"Employee id assigned to this profile is: {emp_id}")
        emp_id += 1
        input_exit = input("Do you want to add another profile? (yes/no): ")
        if input_exit == "no":
            print("Successfully added.")
            break

def read():
    print("Do you want to read all profiles or an individual profile?")
    read_input = input("Press 1 for an individual profile and 2 for all: ")
    if read_input == "1":
        emp_id = int(input("Enter the employee ID: "))
        if emp_id in employee_data:
            print(f"Employee ID: {emp_id}, Data: {employee_data[emp_id]}")
        else:
            print("Employee not found.")
    elif read_input == "2":
        for emp_id, data in employee_data.items():
            print(f"Employee ID: {emp_id}, Data: {data}")
    else:
        print("Invalid option.")

def exit_menu():
    print("Exiting the program. Thank you!")
    exit()

def update_profile():
    emp_id = int(input("Enter the employee ID to update: "))
    if emp_id in employee_data:
        prev = employee_data[emp_id]
        print(f"Employee ID: {emp_id}, Data: {employee_data[emp_id]}")
        print("Enter details to update :")
        name = input("Enter employee name: ")
        if name == "":
            name = prev.get('name')
        location = input("Enter employee location: ")
        if location == "":
            location = prev.get('location')
        salary = input("Enter employee salary: ")
        if salary == "":
            salary = prev.get('salary')
        age = input("Enter employee age: ")
        if age == "":
            age = prev.get('age')
        employee_data[emp_id] = {
            "name": name,
            "location": location,
            "salary": salary,
            "age": age
        }
        print(f"Employee ID: {emp_id}, Data: {employee_data[emp_id]}")
        print("Profile updated successfully.")
    else:
        print("Profile does not exist.")

def delete_profile():
    emp_id = int(input("Enter the employee ID to delete: "))
    if emp_id in employee_data:
     print(f"Employee ID: {emp_id}, Data: {employee_data[emp_id]}")
     del employee_data[emp_id]
     print("delete profile successfully")
    else:
        print("print not existed :")

def age_identifier():
    print("age identifier")
    emp_id = int(input("Enter the employee ID to age identify: "))
    name = employee_data[emp_id].get('name')
    age = employee_data [emp_id].get('age')
    if age >= 25 :
        print(f"{name}:employe is not young and age:{age}")
    elif age <= 25 :
        print(f"{name}:employee is young and age:{age}")

def adrress_locate():
    op = input("press 1 for location wise address and 2 for indivual adrress:")
    if op == '1':
        location = input("Enter location: ")
        for emp_id, data in employee_data.items():
            if location in data.get('location'):
                print(f"Employee ID: {emp_id}, Data: {data}")
    
    elif op == '2':
        emp_id = int(input("Enter the employee ID to check the address: "))
        if emp_id in employee_data:
          name = employee_data[emp_id].get('name')
          location = employee_data[emp_id].get('location') #getting specicfic item from list through dict

        if location == 'islamabad':
            print(f"{name}:employee is belong :{location}")
                    
        elif location == 'lahore':
            print(f"{name}:employee is belong :{location}")
           
        elif location == 'karachi':
            print(f"{name}:employee is belong :{location}")
        else :
            print(f"{name}:employee is belong to unkown area:")
    else:
             print("id not existed :")

def salary():

    emp_id = int(input("Enter the employee ID to check salary: "))
    if emp_id in employee_data:
        salary = employee_data[emp_id].get('salary')
        name = employee_data[emp_id].get('name') 
        print (f"{name}: current salary: {salary}")

    else:
        print("Employee not found.")

def name():
     
    emp_id = int(input("Enter the employee ID to check the name characters : "))
    if emp_id in employee_data:
        name = employee_data[emp_id].get('name') # accessing dictionary
        print(f"name: {name}")
        length = len(name)# len is used to find legnth 
        print(f"the length of the characters in name:{length}")
    else:
        print("print not existed :")

def age():

    print("age checker youngest and oldest employee:")
    ages = [item['age'] for item in employee_data.values()] # imp line accessing age from all list item 
    print(f"all employee ages:{ages}")
    print(f"maximum age employe :{max(ages)}")
    print(f"minimum age employe :{min(ages)}")
