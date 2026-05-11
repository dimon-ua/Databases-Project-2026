import mysql_connection
import db_operations 


def display_menu():
    print("Conference Management")
    print("---------------------")
    print("\n")
    print("MENU")
    print("====")
    print("1. View Speakers & Sessions")
    print("2. View Attendees by Company")
    print("3. Add New Attendee")
    print("4. View Connected Attendees")
    print("5. Add Attendee Connection")
    print("6. View Rooms")
    print("x. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            print("\n")
            x = input("Enter speaker name : ")
            print(f"Session Details for : {x}")
            db_operations.view_speakers_sessions(x)
            
        if choice == '2':
            while True:
                company_id = input("Enter company ID : ")
                
                if company_id.isdigit() and int(company_id) > 0:
                    db_operations.attendees_by_company(company_id)   
                    break;
                else:
                    company_id = input("Enter company ID : ")                 
        
        if choice == '3':
            print("Add new Attendee\n")
            print("------------------")
            attendee_id = input("Attendee ID : ")
            attendee_name = input("Name : ")
            attendee_dob = input("DOB : ")
            attendee_gender = input("Gender : ")
            attendee_company_id = input("Company ID : ")
            
            db_operations.add_new_attendee(attendee_id, attendee_name, attendee_dob, attendee_gender, attendee_company_id)
                    
        if choice == '4':
            attendee_id = input("Enter Attendee ID : ")
            
            if not attendee_id.isdigit():
                print("*** ERROR *** Invalid attendee ID")
            else:
                db_operations.view_connected_attendees(attendee_id)
                
        if choice == '5':
            while True:
                id1 = input("Enter Attendee 1 ID : ")
                id2 = input("Enter Attendee 1 ID : ")
                
                if not id1.isdigit() or not id2.isdigit():
                    print("*** ERROR *** Attendee IDs must be numbers")
                    continue
                
                if db_operations.add_attendee_connection(id1, id2):
                    break
                    
        if choice == '6':
            db_operations.view_rooms()
            
        
        if choice == 'x':
            break
        else:
            pass
            #print(f"You selected {choice}")

if __name__ == "__main__":
    main()
    
