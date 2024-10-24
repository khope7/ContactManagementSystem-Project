#Your task is to develop a Contact Management System with the following features:
# User Interface (UI):
#Create a user-friendly command-line interface (CLI) for the Contact Management System.
#Display a welcoming message and provide a menu with the following options:
#Welcome to the Contact Management System! 
#Menu:
#1. Add a new contact
#2. Edit an existing contact
#3. Delete a contact
#4. Search for a contact
#5. Display all contacts
#6. Export contacts to a text file
#7. Import contacts from a text file *BONUS*
#8. Quit
#Contact Data Storage:
#Use nested dictionaries as the main data structure for storing contact information.
#Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#Store contact details within the inner dictionary, including:
#Name
#Phone number
#Email address
#Additional information (e.g., address, notes).
#Menu Actions:
#Implement the following actions in response to menu selections:
#Adding a new contact.
#Editing an existing contact's information (name, phone number, email, etc.).
#Deleting a contact.
#Searching for a contact and displaying their details.
#Displaying a list of all contacts.
#Exporting contacts to a text file in a structured format.
#Importing contacts from a text file and adding them to the system. * BONUS
#User Interaction:
#Utilize input() to enable users to select menu options and provide contact details.
#Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
#Error Handling:
#Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
#GitHub Repository:
#Create a GitHub repository for your project.
#Create a clean and interactive README.md file in your GitHub repository.
#Include clear instructions on how to run the application and explanations of its features.

#Writing code for ContactManagementSystem

#Importing regex for regex functionality
import re

#Importing os module for file allocation
import os

#Instantiating contacts list as a Nested Dictionary
contact_list = {}

#Creating user interface function to introduce gui and take in choices of 1-8 
def user_interface():
#Creating while loop to ask for user re entry
    while True:
#Using try except block to catch for all other entries
        try:
            choice = int(input('''Welcome to the Contact Management System 
    Menu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file *BONUS*
    8. Quit
    
    Please choose any option: '''))
            
#Catches integers outside of range 1-8 and any alpha entries
            if choice < 1 or choice > 8:
                print("Unable to proceed, choice must be between 1 and 8. Please try again.")

            elif choice == 1:
                add_contacts()
                break
            elif choice == 2:
                edit_contacts()
                break
            elif choice == 3:
                delete_contacts()
                break
            elif choice == 4:
                search_contacts()
                break
            elif choice == 5:
                display_contacts()
                break
            elif choice == 6:
                export_contacts()
                break
            elif choice == 7:
                import_contacts()
                break
            elif choice == 8:
                quit_system()
                break
        except ValueError:
            print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")

#Creating add contacts function to take in values for contact list            
def add_contacts():
#Taking in name variable for dictionary and adjusting case for every name entry
    name = input("Please enter new contact name: ")
    name = name.title()
#Created try block to catch for first entry KeyError for existing value check
    try:
#Created if then statement to add '+' for additional name entries to avoid contact replacement upon same name entry
        if  name == contact_list[name]["Name"]:
            ask = input("That name is already entered, would you like to create new instance? type (yes/no): ")
            if ask.lower() == "yes" or ask.lower() == "ok" or ask.lower() == "y":
                name = name + "+"
                print(f"Thank you, name: {name}")
            elif ask.lower() == "no" or ask.lower() == "n" or ask.lower() == "no thanks":
                add_contacts()
            else:
                print("Apologies, entry must be a yes/y or no/n")
                add_contacts()
                
#Else statment created for first time name entries
        else:
            print(f"Thank you, name: {name}")
    except KeyError:
        print(f"Thank you, name: {name}")
        
#Created while loop to ask for user re entry after erroneous entries
    while True:
        test_number = input("Please enter new contact phone number:")
#Created if statement to add test_number as number value if entered in standard format
        if re.search(r"\d{3}-\d{3}-\d{4}", test_number):
#Using regex find standard number within string of input entry, converting to string format and printing
            list_number = re.findall(r"\d{3}-\d{3}-\d{4}", test_number)
            number = ''.join(list_number)
            print(f"Thank you, number: {number}")
            break
#Using regex to find full number within string of input entry, converting to string and printing
        elif re.search(r"\d{10}", test_number):
            full_list_number = re.findall(r"\d{10}", test_number)
            find_number = ''.join(full_list_number)
#After creating string of 10 digit TN within string, used slicing to convert full digit TN into standard format
#https://stackoverflow.com/questions/67977392/how-do-i-split-a-list-of-numbers-into-a-phone-number-in-python for refrence
            number = (f"{find_number[:3]}-{find_number[3:6]}-{find_number[6:10]}")
            print(f"Thank you, number: {number}")
            break
#Used else statment to catch for any non TN entries
        else:
            print("Apologies, number must be in XXX-XXX-XXXX format or XXXXXXXXXX format\n")

#Created while loop to ask for user re entry for any non email ('name@domain.com') entries and printing
    while True:
        test_email = input("Please enter new contact email: ")
        if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", test_email):
            email = test_email
            print(f"Thank you, email: {email}")
            break
        else:
            print("Apologies, email entry must be in 'name@domain.com' format")

#Creating string for additional info value and printing
    additional_info = input("Any additional info?: ")
    print(f"Thank you, additional info: {additional_info}")

#Adding full contact into contact list as a nested dictionary element
    contact_list[name] = {"Name" : name, "Phone Number" : number, "Email" : email, "Additional Info" : additional_info}

#Returning user to Contact Management System
    user_interface()

#Creating edit_contacts function to edit contacts
def edit_contacts():
#Instantiating while loop for user reentry
    while True:
#Using for loop to print current contacts in user friendly format
        print("Current contacts:")
        for contacts, contact in contact_list.items():
            print(f"{contacts}"+ " " + f"{contact}")
#Asking user to choose which contact to update
        contact_choice = input("Please enter the name of the contact you would like to update: ")
#Reinstantiating user input as a title
        contact_choice = contact_choice.title()
#Runs if statement only if the contact user entered is in the contact list dict
        if contact_choice in contact_list:
#Asking user to choose what of that contact they would like to update
            edit_choice = input("Contact found, what would you like to update?: type: (name/number/email/info): ")
            edit_choice = edit_choice.title()
#If statment that runs if name or Name is entered
            if edit_choice == "Name":
#Creating variable for user input name choice for the name they would like to change this contact to be
                name_choice = input("What name would you like the new name to be?: ")
                name_choice = name_choice.title()
#Using for loop to seek contacts in contact list to see if the updating name is already in the contact list
                for contacts in contact_list:
                    if name_choice not in contacts:
#Changes initial Name key value to the name entered for update from the contact choice from user contact choice entry by accessing key from specific for loop within contact list dictionary
                        contact_list[contact_choice]["Name"] = name_choice
#Finds initial element for dictionary currently being accessed in for loop and updates the dict name by deleting and updating with corrected name_choice entry
                        contact_list[name_choice] = contact_list.pop(contact_choice)
#Creating user confirmation and reprinting updated contact list in user friendly format and breaks loop
                        print(f"Changed {contact_choice} to {name_choice}")
                        for key, value in contact_list.items():
                            print(f"{key}: {value}")
                        break
#Returns user back to while loop if name_choice is not unique
                    elif name_choice in contact_list:
                        print("Apologies, your name choice must be unique, please try again.")

#If statment that runs if number or Number is entered
            elif edit_choice == "Number":
#Created while loop to ask for user re entry after erroneous entries
                while True:
                    tnumber_choice = input("Please enter new contact phone number: ")
                    if re.search(r"\d{3}-\d{3}-\d{4}", tnumber_choice):
                        new_number = re.findall(r"\d{3}-\d{3}-\d{4}", tnumber_choice)
                        n_number = ''.join(new_number)
                        contact_list[contact_choice]["Number"] = n_number
                        print(f"Thank you, the number for {contact_choice} has been updated to: {n_number}")
                        break

                    elif re.search(r"\d{10}", tnumber_choice):
                        full_new_number = re.findall(r"\d{10}", tnumber_choice)
                        full_number = ''.join(full_new_number)
                        ftnumber = (f"{full_number[:3]}-{full_number[3:6]}-{full_number[6:10]}")
                        contact_list[contact_choice]["Number"] = ftnumber
                        print(f"Thank you, the number for {contact_choice} has been updated to: {ftnumber}")
                        break
#Used else statment to catch for any non TN entries
                    else:
                        print("Apologies, number must be in XXX-XXX-XXXX format or XXXXXXXXXX format\n")

#If statment that runs if email or Email is entered
            elif edit_choice == "Email":
                while True:
                    new_email = input("Please enter new email: ")
                    if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", new_email):
                        email_update = new_email
                        contact_list[contact_choice]["Email"] = email_update
                        print(f"Thank you, the email for {contact_choice} has been updated to: {email_update}")
                        break
                    else:
                        print("Apologies, email entry must be in 'name@domain.com' format")

#If statment that runs if email or Email is entered
            elif edit_choice == "Info":
                new_info = input("What would you like to replace additional info with?: ")
                contact_list[contact_choice]["Info"] = new_info
                print(f"Thank you, the email for {contact_choice} has been updated to: {new_info}")                       
                        

#Returns user back to while loop if contact name is not in contact list
        else:
            print("Apologies, your name choice must be a contact in your contact list, please try again.")
#Returns user back to user interface menu and breaks loop 
        user_interface()
        break

#Creating function to delete contacts from contact_list
def delete_contacts():
#Instantiating while loop for user reentry
    while True:
#Printing current contacts in user friendly format
        print("Current contacts:")
        for contacts, contact in contact_list.items():
            print(f"{contacts}"+ " " + f"{contact}\n")
#Asking user for contact to delete and adjusting entry into title form
        delete_choice = input("Please enter the name of the contact you would like to delete: ")
        delete_choice = delete_choice.title()
#Created if statement to proceed only if the choice user wants to delete is in the contact list
        if delete_choice in contact_list:
#Using delete method to delete dictionary of choice matching contact list dictionary name
            del contact_list[delete_choice]
#Printing confirmation and updated contact list in user friendly format
            print(f"{delete_choice} has been deleted.")
            print("Current contacts:")
            for key, value in contact_list.items():
                print(f"{key}: {value}")
#Returns user back to user interface menu and breaks loop
                user_interface()
                break
#Returns user back to while loop if contact delete choice not in contact list
        else:
            print("Apologies, your name choice must be a contact in your contact list, please try again.")


#Creating search contacts function to display contact attributes upon user search request
def search_contacts():
    while True:
#Creating for loop to show list of contacts via dictionary name
        print("Current contacts:")
        for contacts in contact_list.items():
            print(f"{contacts}")
#Asking for user entry to display attributes for mentioned dictionary
        search_choice = input("Please enter the name of the contact you would like to see in detail: ")
        search_choice = search_choice.title()
#Printing users search choice in friendly formatt
        if search_choice in contact_list:
            print(f"Here are {search_choice}'s details:\n{search_choice}\n{contact_list[search_choice]}\n")
            user_interface()
            break
#Returns user back to while loop if contact search choice not in contact list
        else:
            print("Apologies, your name choice must be a contact in your contact list, please try again.")
        
#Creating display contacts function to show full contact list
def display_contacts():
    print(f"Here is your current contact list:")
    for contacts, contact in contact_list.items():
        print(f"{contacts}"+ " " + f"{contact}")
    user_interface()

#Creating export contacts function to write in contact list to a new file
def export_contacts():
#Using try except method to account for file access write and print errors
    try:
        ask = input("Are you sure you would like to export contacts? type (yes/no): ")
        if ask.lower() == "yes" or ask.lower() == "ok" or ask.lower() == "y":
#If no file exists, creates file in current folder and writes contact by nested dictionary
            with open('ContactManagementList.txt', 'w') as file:
                for contacts, contact in contact_list.items():
                    file.write(f"{contacts}"+ " " + f"{contact}" + "\n")
#Printing confirmation and returning user to main menu
            print(f"Thank you, contact list exported to current folder")
            user_interface()

        elif ask.lower() == "no" or ask.lower() == "n" or ask.lower() == "no thanks":
            user_interface()
        else:
            print("Apologies, entry must be a yes/y or no/n")
            export_contacts()

#Created to catch for permission errors
    except PermissionError:
        print("You dont have permission to write to this file")
        user_interface()
#Created to catch for errors occured while writing
    except IOError:
        print("An issue occurred while writing to the file")
        user_interface()
#Created to catch for file not existing
    except FileNotFoundError:
        print("The file doesnt exist!")
        user_interface()
#Created for all other possible errors
    except Exception as e:
        print(f"A general error occurred: {e}")
        user_interface()

#Created function to import contacts additional txt file with try except block to catch for all possibilities
def import_contacts():
    ask = input("Are you sure you would like to import contacts? type (yes/no): ")
    try:
        if ask.lower() == "yes" or ask.lower() == "ok" or ask.lower() == "y":
#If file exists, imports text from txt file as str and prints by new line to show for full contact list in readable format
            with open("ContactManagementList.txt", 'r') as file:
                contact_import = file.read()
#Using split method from new line break to recreate individual dictionaries as str contacts and printing
                updated_import = contact_import.split('\n')
#Using for loop for readable format                
                for imported_contact in updated_import:
                    print(imported_contact)

            print(f"Thank you, contact list imported to current folder")
            user_interface()

        elif ask.lower() == "no" or ask.lower() == "n" or ask.lower() == "no thanks":
            user_interface()
        else:
            print("Apologies, entry must be a yes/y or no/n")
            import_contacts()

#Created to catch for permission errors
    except PermissionError:
        print("You dont have permission to write to this file")
        user_interface()
#Created to catch for errors occured while writing
    except IOError:
        print("An issue occurred while writing to the file")
        user_interface()
#Created to catch for file not existing
    except FileNotFoundError:
        print("The file doesnt exist!")
        user_interface()
#Created for all other possible errors
    except Exception as e:
        print(f"A general error occurred: {e}")
        user_interface()

#Created quit system function to exit system
def quit_system():
#Using built in exit function to exit run or return to main menu on reask request
    ask = input("Are you sure you would like to quit? type (yes/no): ")
    if ask.lower() == "yes" or ask.lower() == "ok" or ask.lower() == "y":
        print(f"Thank you, exiting.")
        exit()
    elif ask.lower() == "no" or ask.lower() == "n" or ask.lower() == "no thanks":
        user_interface()
    else:
        print("Apologies, entry must be a yes/y or no/n")
        quit_system()

#Calling user_interface function for initial run
user_interface()