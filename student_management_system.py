# List of students with their details
student_list = []

# Function to create a new entry for a student
def New_Entry():
    # Print message indicating the start of creating a new entry
    print("---CREATE NEW ENTRY---")
    # Initialize a flag to check if the student already exists
    res = False
    # Prompt the user to input student details
    name = input("Name: ")
    lastname = input("Lastname: ")
    father_name = input("Father's Name: ")

    # Check if a student with the provided details already exists
    for i in range(len(student_list)):
        if student_list[i]["name"] == name and student_list[i]["lastname"] == lastname and student_list[i]["fathername"] == father_name:
            # If a student with the same details exists, print their details and set the flag to True
            print("There is already a student with these information\n")
            # Print the existing student's details
            for key in student_list[i].keys():
                print(f"{key} --> {student_list[i][key]}")
            res = True

    # Continue the process if the student does not exist
    while res:
        # Prompt the user to continue or return to the menu
        continue_creation = input("Continue? (Y/N): ")
        # Validate the user input
        if continue_creation.lower() != "y" and continue_creation.lower() != "n":
            continue_creation = input("Continue? (Y/N): ")
        if continue_creation.lower() == "n":
            # If the user chooses not to continue, set the flag to False and return to the menu
            res = False
            print("Returning you to the menu...")
            Menu()

    # Prompt the user to input age, ensuring it is a positive integer
    while True:
        age = (input("Age: "))
        if age.isdigit() and age > "0":
            break

    # Prompt the user to input class, ensuring it is a digit between 1 and 5
    while True:
        school_class = (input("Class(1,2,3,4,5): "))
        if school_class.isdigit() and (school_class > "0" and school_class < "6"):
            break

    # Prompt the user to input number ID, ensuring it follows the specified format
    while True:
        number_id = input("Number ID (Space if None): ")
        if not number_id.isspace():
            if number_id.isalnum() and len(number_id) == 8:
                break
            else:
                print("Number ID should be in this format --> AA123456")
        else:
            number_id = None
            break

    # Generate a unique ID for the new student entry
    id = 1001 + len(student_list)
    # Add the new student to the list
    student_list.extend(
        [
            {"id": id,
            "name": name,
            "lastname": lastname,
            "fathername": father_name,
            "age": age,
            "class": school_class,
            "number_id": number_id}
        ]
    )
    # Print message indicating the successful creation of the new entry
    print("---NEW ENTRY CREATED---")
    # Print the details of the new student entry
    for key in student_list[3].keys():
        print(f"{key} = {student_list[3][key]}")
    # Return to the main menu
    Menu()

# Function to print student details by ID
def Print_Entry():
    # Loop until valid input is provided for viewing all or one entry
    while True:
        # Prompt the user to choose to view all or one entry
        all_or_one = input("View ALL or ONE entry?(ALL/ONE): ")
        # Check if the input is alphabetic and within valid options
        if all_or_one.isalpha() and (all_or_one.lower() == "one" or all_or_one.lower() == "all"):
            break

    # If the user chooses to view one entry
    if all_or_one.lower() == "one":
        # Loop until valid student ID input is provided
        while True:
            student_id = input("Write the student's ID: ")
            # Check if the input is a digit and within a valid range and length
            if student_id.isdigit() and (student_id > "1000" and student_id < "2000") and len(student_id) == 4:
                break
            else:
                print("Student ID should have this format: (1001),(1002)...")
        # Iterate through the student list to find the student by ID
        for student in student_list:
            # If the student is found, print their entry details
            if student["id"] == student_id:
                print("---STUDENT ENTRY---")
                # Iterate through the key-value pairs of the student entry and print them
                for key, value in student.items():
                    print(f"{key} --> {value}")
                # Return to the main menu
                Menu()
    # If the user chooses to view all entries
    else:
        # Iterate through the student list and print each entry
        for i in range(len(student_list)):
            print(f"\n----------\nEntry Number {i+1}\n----------")
            for key in student_list[i].keys():
                print(f"{key} --> {student_list[i][key]}")
        Menu()
    # Print a message indicating that the student is not found (this should not occur for viewing all entries)
    print("Student not found!")
    # Return to the main menu
    Menu()


# Function to update student details by ID
def Update_Entry():
    # Initialize a boolean variable to track if the student ID is found in the student list
    found = False

    # Prompt the user to input the student's ID
    student_id = input("Write the student's ID: ")

    # Initialize a variable to hold the index of the found student entry in the student list
    i_holder = 0

    # Iterate through the student list to find the student by ID
    for i in range(len(student_list)):
        # Check if the current student's ID matches the input student ID
        if student_list[i]["id"] == student_id:
            # If the student is found, print their entry details
            print("---STUDENT ENTRY---")
            for key in student_list[i]:
                # Print each key-value pair in the student entry
                print(f"{key} --> {student_list[i][key]}")
            # Save the index of the found student entry
            i_holder = i
            # Set the found flag to True
            found = True

    # If the student is not found in the list, print an error message
    if not found:
        print("----------\nERROR 404! Student not found!\n----------")
        Menu()

    # Update student information
    info_update = input("""\n----------\nWhat info do you want to update?
        ID --> Student ID
        N --> Name
        L --> Lastname
        F --> Father's Name
        A --> Age
        C --> Class
        NID --> Number ID

Write here: """)
    if info_update.lower() == "id":
        # Delete old student ID and update with new ID
        student_list[i_holder]["id"] = input("Write the NEW ID: ")
        print("---ID UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "n":
        #Delete old student Name and update with new Name
        student_list[i_holder]["name"] = input("Write the NEW NAME: ")
        print("---NAME UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "l":
        #Delete old student Name and update with new Name
        student_list[i_holder]["lastname"] = input("Write the NEW LASTNAME: ")
        print("---LASTNAME UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "f":
        #Delete old student Name and update with new Name
        student_list[i_holder]["fathername"] = input("Write the NEW FATHER'S NAME: ")
        print("---FATHER'S NAME UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "a":
        #Delete old student Name and update with new Name
        while True:
            student_list[i_holder]["age"] = input("Write the NEW AGE: ")
            if student_list[i_holder]["age"].isdigit() and student_list[i_holder]["age"] > "0":
                break
        print("---AGE UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "c":
        #Delete old student Name and update with new Name
        while True:
            student_list[i_holder]["class"] = input("Write the NEW CLASS: ")
            if student_list[i_holder]["class"].isdigit() and (student_list[i_holder]["class"] > "0" and student_list[i_holder]["class"] < "6"):
                break
        print("---CLASS UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    elif info_update.lower() == "nid":
        #Delete old student Name and update with new Name
        while True:
            student_list[i_holder]["number_id"] = input("Write the NEW NUMBER ID: ")
            if not student_list[i_holder]["number_id"].isspace():
                if student_list[i_holder]["number_id"].isalnum() and len(student_list[i_holder]["number_id"]) == 8:
                    break
                else:
                    print("Number ID should be in this format --> AA123456")
            else:
                student_list[i_holder]["number_id"] = None
                break
        print("---NUMBER ID UPDATED---")
        for key in student_list[i_holder]:
                print(f"{key} --> {student_list[i_holder][key]}")
        Menu()
    
def Delete_Entry():
    # Flag to track if the student ID is found
    found = False
    
    # Get the student ID from the user
    student_id = input("Write the student's ID: ")
    
    # Index holder for the found student entry
    i_holder = 0
    
    # Iterate through the student list to find the student by ID
    for i in range(len(student_list)):
        if student_list[i]["id"] == student_id:
            # If the student is found, print their details
            print("---STUDENT ENTRY---")
            for key in student_list[i]:
                print(f"{key} --> {student_list[i][key]}")
                i_holder = i  # Save the index of the found student
            found = True  # Set the flag to True indicating the student is found
    
    # If the student is not found, print an error message and return to the menu
    if not found:
        print("----------\nERROR 404! Student not found!\n----------")
        Menu()
    
    # Prompt the user for deletion option
    while True:
        delete_question = input("Delete everything (1) or specific entry(2)? Write the corresponding number: ")
        if delete_question.isdigit() and delete_question in ("1", "2"):
            # If user chooses to delete everything
            if delete_question == "1":
                while True:
                    yes_no = input("Are you sure? (Y/N): ")
                    if yes_no.lower() in ("y", "n"):
                        if yes_no.lower() == "y":
                            # Clear the entry and remove it from the list
                            student_list[i_holder].clear()
                            student_list.pop(i_holder)
                            print("---ENTRY DELETED---")
                            for key in student_list[i_holder]:
                                print(f"{key} --> {student_list[i_holder][key]}")
                            break
                        else:
                            Menu()
            else:
                # Prompt user for which entry to delete
                info_delete = input("""\n----------\nWhat info do you want to delete?
        ID --> Student ID
        N --> Name
        L --> Lastname
        F --> Father's Name
        A --> Age
        C --> Class
        NID --> Number ID

Write here: """)
                if info_delete.lower() == "id":
                    # Delete old student ID and update with None
                    student_list[i_holder]["id"] = None
                    print("---ID DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "n":
                    #Delete old student Name and update with None
                    student_list[i_holder]["name"] = None
                    print("---NAME DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "l":
                    #Delete old student Name and update with None
                    student_list[i_holder]["lastname"] = None
                    print("---LASTNAME DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "f":
                    #Delete old student Name and update with None
                    student_list[i_holder]["fathername"] = None
                    print("---FATHER'S NAME DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "a":
                    #Delete old student Name and update with None
                    student_list[i_holder]["age"] = None
                    print("---AGE DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "c":
                    #Delete old student Name and update with None
                    student_list[i_holder]["class"] = None
                    print("---CLASS DELETED---")
                    print (student_list[i_holder])
                    Menu()
                elif info_delete.lower() == "nid":
                    #Delete old student Name and update with None
                    student_list[i_holder]["number_id"] = None
                    print("---NUMBER ID DELETED---")
                    print (student_list[i_holder])
                    Menu()
    
# Function for the menu
def Menu():
    # Menu options
    menu = '''-----------Menu-----------
|  1. Create new entry   |
--------------------------
|        2. Print        |
--------------------------
|  3. Update entry       |
--------------------------
|     4. Delete entry    |
--------------------------
|        5. Exit         |
--------------------------'''
    print(menu)
    while True:
        # Get user choice
        menu_choice = int(input("What would you like to do? Select the corresponding number: "))
        if menu_choice > 1 and menu_choice <= 5:
            break
    # Perform action based on user choice
    if menu_choice == 1:
        New_Entry()
    elif menu_choice == 2:
        Print_Entry()
    elif menu_choice == 3:
        Update_Entry()
    elif menu_choice == 4:
       Delete_Entry()  # Placeholder for delete function
    else:
        exit()

Menu()
